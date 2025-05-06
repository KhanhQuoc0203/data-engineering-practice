import zipfile
import os
from io import TextIOWrapper
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from datetime import datetime


def read_zipped_csvs(spark, zip_dir):
    dfs = []
    for zip_file in os.listdir(zip_dir):
        if zip_file.endswith('.zip'):
            zip_path = os.path.join(zip_dir, zip_file)
            with zipfile.ZipFile(zip_path, 'r') as archive:
                for filename in archive.namelist():
                    if filename.endswith('.csv'):
                        with archive.open(filename) as file:
                            df = spark.read.csv(TextIOWrapper(file, 'utf-8'), header=True, inferSchema=True)
                            dfs.append(df)
    return dfs[0].unionByName(*dfs[1:]) if dfs else None


def save_report(df, name):
    output_path = f'reports/{name}.csv'
    df.coalesce(1).write.mode('overwrite').option('header', 'true').csv(output_path)


def average_trip_duration_per_day(df):
    return df.withColumn("date", to_date("start_time")) \
             .groupBy("date") \
             .agg(avg("tripduration").alias("avg_trip_duration"))


def trips_per_day(df):
    return df.withColumn("date", to_date("start_time")) \
             .groupBy("date") \
             .agg(count("*").alias("trip_count"))


def most_popular_start_station_per_month(df):
    return df.withColumn("month", date_format("start_time", "yyyy-MM")) \
             .groupBy("month", "from_station_name") \
             .agg(count("*").alias("trip_count")) \
             .withColumn("rank", row_number().over(Window.partitionBy("month").orderBy(desc("trip_count")))) \
             .filter(col("rank") == 1).drop("rank")


def top_3_stations_last_2_weeks(df):
    max_date = df.select(max(to_date("start_time"))).collect()[0][0]
    start_date = max_date - timedelta(days=14)

    return df.withColumn("date", to_date("start_time")) \
             .filter(col("date") >= lit(start_date)) \
             .groupBy("date", "from_station_name") \
             .agg(count("*").alias("trip_count")) \
             .withColumn("rank", row_number().over(Window.partitionBy("date").orderBy(desc("trip_count")))) \
             .filter(col("rank") <= 3).drop("rank")


def avg_trip_duration_by_gender(df):
    return df.groupBy("gender") \
             .agg(avg("tripduration").alias("avg_trip_duration"))


def top_10_ages_by_trip_duration(df):
    this_year = datetime.now().year
    df_with_age = df.withColumn("age", lit(this_year) - col("birthyear"))

    longest = df_with_age.orderBy(desc("tripduration")).select("age", "tripduration").limit(10)
    shortest = df_with_age.filter(col("tripduration") > 0).orderBy("tripduration").select("age", "tripduration").limit(10)

    return longest, shortest


def main():
    spark = SparkSession.builder.appName("Exercise6").getOrCreate()

    df = read_zipped_csvs(spark, "data")
    if df is None:
        print("No data found.")
        return

    save_report(average_trip_duration_per_day(df), "avg_trip_duration_per_day")
    save_report(trips_per_day(df), "trips_per_day")
    save_report(most_popular_start_station_per_month(df), "popular_start_station_per_month")
    save_report(top_3_stations_last_2_weeks(df), "top3_stations_last_2_weeks")
    save_report(avg_trip_duration_by_gender(df), "avg_trip_duration_by_gender")

    longest, shortest = top_10_ages_by_trip_duration(df)
    save_report(longest, "top10_longest_trip_ages")
    save_report(shortest, "top10_shortest_trip_ages")

    spark.stop()


if __name__ == "__main__":
    main()
