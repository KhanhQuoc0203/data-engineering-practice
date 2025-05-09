### Báo cáo kết quả các bài tập đã làm được của nhóm 
Bài tập <br> 
Báo cáo <br>
Lap 8:

Lap 9:

Exercise-1 Các thành viên đã hoàn chỉnh file *main.py* trong folder của bài tập này. Khi chạy code thì đã tải và giải nén thành công các file trong các URL ban đầu vào folder *downloads* như đề bài yêu cầu, ngoại trừ file *Divvy_Trips_2220_Q1.zip* là bị lỗi không giải nén được. 
Kết quả:<br> 
![Ex1](https://github.com/user-attachments/assets/be486189-d152-423b-bcc6-902b220e54c3)




Exercise-2 Các thành viên trong nhóm tìm URL chứa file ghi thông tin khí tượng tại *10:27 ngày 19-01-2024* bằng cách sử dụng *BeautifulSoup* để phân tích cú pháp HTML trả về, tìm được file ghi thông tin khí tượng tại *10:27 ngày 19-01-2024* trong 1 tag \<tr> bên trong \<table>. Sau đó tải về và dùng *Pandas* giải quyết yêu cầu của đề bài. 
![Ex2](https://github.com/user-attachments/assets/cc0a48c6-7b68-4c74-9819-68cec511fede)


 Exercise-3 Ở bài tập này các thành viên đã dùng các thư viện phù hợp để tải file thứ nhất về tìm URL và tải file thứ 2 về, tuy nhiên file này có chứa nhiều bảng mã của các ngôn ngữ khác nhau nên quá trình giải mã khá phức tạp. Quá trình in ra nội dung của file thứ 2 khá lâu vì file có dung lượng lớn. <br>
 ![Ex3](https://github.com/user-attachments/assets/9db4ed8d-10e0-4cb8-b487-2d58a4c77c9a)

Exercise-4 Các thành viên đã sử dụng các thư viện phù hợp để tìm các file *.json* trong folder *data*, sau đó chuyển chúng sang file *.csv* bằng các phép biến đổi. 

![Ex4](https://github.com/user-attachments/assets/69761a93-afc8-4fff-bd83-1275c97b5fed)


Exercise-5 Đối với bài tập này, các thành viên đã vận dụng kiến thức, kĩ năng về *Docker* kết hợp với *truy vấn cơ sở dữ liệu* để viết các hàm *kết nối, tạo bảng, ghi dữ liệu* vào cơ sở dữ liệu trên *Postgres* bằng cách sử dụng các *thư viện Python* phù hợp. 
Pipeline Nhóm thống nhất sử dụng Airflow để triển khai pipeline, dùng PostgreSQL để làm cơ sở dữ liệu. Trước tiên, nhóm đã xây dựng file docker-compose để định nghĩa các service có liên quan tới container, nhóm thống nhất định nghĩa service postgres của Exercise-5 vào chúng file docker-compose cho pipeline. Có 1 điểm khác biệt so với khi làm bài tập cá nhân là nhóm đã giới hạn lại số URL để tải file ở Exercise-1 xuống còn 1, ở Exercise-3 nhóm giới hạn chỉ in ra 10000 dòng của file thứ 2 để đỡ tốn thời gian. Sau đó chạy container của pipeline ![](/images/ketqua.png) <br>
![Ex5](https://github.com/user-attachments/assets/a0a9b0b4-43da-4d51-863e-40f281a880f5)


Exercise-6 Thành viên sử dụng thư viện pyspark để hoàn thành phần này, đọc từ 2 file zip mà không cần giải nén, trả lời 6 câu hỏi của bài và được lưu trong thư mục requests
![Ex6](https://github.com/user-attachments/assets/876d2eaf-204e-4bef-9f14-053f485036a7)


| Exercise-7 | Mỗi thành viên đã sử dụng thư viện riêng phù hợp của pyspark để hoàn thành bài tập này, file data bên trong đã được các thư viện ấy xử lý. từng thành viên đã hoàn thành được:Thêm tên tệp dưới dạng một cột, Kéo phần datenằm bên trong chuỗi của source_filecột, Thêm một cột mới có tên là brand, Kiểm tra một cột có tên là capacity_bytes, Tạo một cột có tên primary_keylà hashcột tạo nên bản ghi umique trong tập dữ liệu này.
![Ex7](https://github.com/user-attachments/assets/776143ea-ed96-4cae-990f-128845fa4b73)

