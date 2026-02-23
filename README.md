# Sorting_Algorithm_Experiment
Bài tập thực nghiệm 4 thuật toán sắp xếp

# Báo cáo thực nghiệm thuật toán sắp xếp

Dự án này chứa mã nguồn và báo cáo cho bài tập thực nghiệm so sánh hiệu năng của các thuật toán sắp xếp trên bộ dữ liệu lớn.

## 1. Thành phần dự án
* `Sorting_experiment.py`: Mã nguồn thực hiện tạo dữ liệu, chạy thử nghiệm và đo thời gian.
* `Sorting_Report.pdf`: Báo cáo chi tiết kết quả dưới dạng bảng, biểu đồ và nhận xét.
* `Dataset.docx`: Thông tin về bộ dữ liệu được sử dụng.

## 2. Các thuật toán thử nghiệm
* **QuickSort**: Thuật toán chia để trị, chọn chốt ở giữa.
* **MergeSort**: Sắp xếp trộn, đảm bảo độ phức tạp ổn định.
* **HeapSort**: Sắp xếp vun đống, sử dụng cấu trúc cây nhị phân.
* **NumPy Sort**: Hàm sắp xếp mặc định của thư viện NumPy.

## 3. Quy mô dữ liệu
* Số lượng: 10 dãy dữ liệu.
* Kích thước: 1,000,000 phần tử/dãy.
* Loại dữ liệu: Số thực và số nguyên.
* Trạng thái: Tăng dần, giảm dần và ngẫu nhiên.

## 4. Cách chạy chương trình
1. Cài đặt thư viện: `pip install numpy`
2. Chạy lệnh: `python sorting_test.py`
