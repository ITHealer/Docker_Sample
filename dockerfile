# FROM python:3.10-alpine sẽ tải xuống image Python 3.10 trên Alpine Linux từ Docker Hub, nó không liên quan đến python version trên máy của mình.
FROM python:3.10-alpine

# WORKDIR /app: Chỉ định thư mục làm việc cho container.
WORKDIR /app

# Khai báo port mà container sẽ lắng nghe
# Nếu app Python của bạn chạy trên port 5000 trong container:
#     Map port 5000 container -> port 5000 host: docker run -p 5000:5000 example_02
#     Map port 5000 container -> port 8080 host: docker run -p 8080:5000 example_02
# Sau khi map port, bạn có thể truy cập ứng dụng từ máy local:
#     Nếu map port 5000: http://localhost:5000
#     Nếu map port 8080: http://localhost:8080
#     Lưu ý:
#         Port bên trái là port trên máy host (máy local của bạn)
#         Port bên phải là port trong container
# Có thể bạn không cần EXPOSE thay vì vậy bạn có thể dùng -p flag khi chạy container
EXPOSE 5000 
# COPY . .: Sao chép tất cả các file từ thư mục hiện tại vào thư mục /app trong container.\
# Dấu . đầu tiên: đại diện cho toàn bộ files/folders trong context directory trên máy local của bạn
# Dấu . thứ hai: đại diện cho thư mục đích trong container (trong trường hợp này là /app vì đã được set bởi WORKDIR)
# Lệnh này sẽ copy các files từ máy local vào thư mục /app trong container
COPY . .

# RUN pip install -r requirements.txt: Cài đặt tất cả các package được liệt kê trong file requirements.txt.
RUN pip install -r requirements.txt

# CMD ["python", "example_01.py"]: Chỉ định lệnh sẽ chạy khi container được khởi chạy.
CMD ["python", "example_02.py"]
