Lab 8:

## 📘 BÀI 1: Pipeline Cào Dữ Liệu và Trực Quan Hóa

### 🎯 Mục tiêu
- Cào dữ liệu tỷ giá từ website: [x-rates.com](https://www.x-rates.com/table/?from=USD&amount=1)
- Lưu dữ liệu tỷ giá vào file `.csv`
- Vẽ biểu đồ trực quan tỷ giá của 10 đơn vị tiền tệ phổ biến
- Tự động hóa bằng script Python (và Docker)

### 🧪 Các bước thực hiện
1. Sử dụng `requests` và `BeautifulSoup` để lấy dữ liệu HTML.
2. Dùng `pandas.read_html()` để trích xuất bảng tỷ giá.
3. Lưu dữ liệu ra `data/rates.csv`
4. Dùng `matplotlib` để vẽ biểu đồ thanh (bar chart) tỷ giá so với USD.

### 📊 Kết quả
- File dữ liệu: `data/rates.csv`
- Biểu đồ: `plots/rates_<ngày>.png`

---

## 🤖 BÀI 2: Pipeline Huấn Luyện Mô Hình Dự Đoán Tỷ Giá

### 🎯 Mục tiêu
- Từ dữ liệu tỷ giá đã cào, huấn luyện mô hình phân loại (tăng/giảm)
- Mô hình: `RandomForestClassifier`
- Gán nhãn:
  - `1` nếu tỷ giá > 1 (tăng)
  - `0` nếu tỷ giá ≤ 1 (giảm)
- Đánh giá độ chính xác và lưu mô hình

### 🧪 Các bước thực hiện
1. Cào dữ liệu từ [x-rates.com](https://www.x-rates.com) tương tự Bài 1
2. Tiền xử lý:
   - Chuyển `Rate` sang float
   - Gán nhãn `Label`
3. Huấn luyện:
   - Train/Test split
   - Train RandomForest
   - Đánh giá `accuracy`
4. Lưu mô hình thành `model/model.pkl` bằng `joblib`
## Ngày hoàn thành
- 06/05/2025
