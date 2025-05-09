import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Tạo thư mục nếu chưa có
os.makedirs("data", exist_ok=True)
os.makedirs("plots", exist_ok=True)

def scrape_exchange_rates():
    url = "https://www.x-rates.com/table/?from=USD&amount=1"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    table = soup.find("table", {"class": "tablesorter ratesTable"})
    df = pd.read_html(str(table))[0]

    df.columns = ["Currency", "Rate", "Inverse"]
    df = df.head(10)  # Lấy 10 dòng đầu tiên

    today = datetime.now().strftime("%Y-%m-%d")
    csv_path = f"data/rates_{today}.csv"
    df.to_csv(csv_path, index=False)
    print(f"✅ Saved to {csv_path}")
    return df, today

def plot_exchange_rates(df, today):
    df["Rate"] = df["Rate"].astype(float)

    plt.figure(figsize=(10, 6))
    plt.barh(df["Currency"], df["Rate"], color="skyblue")
    plt.xlabel("Tỷ giá (so với 1 USD)")
    plt.title(f"Tỷ giá hôm nay ({today})")
    plt.tight_layout()
    plot_path = f"plots/rates_{today}.png"
    plt.savefig(plot_path)
    print(f"📊 Plot saved to {plot_path}")
    plt.close()

def main():
    df, today = scrape_exchange_rates()
    plot_exchange_rates(df, today)

if __name__ == "__main__":
    main()
