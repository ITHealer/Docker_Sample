# FROM python:3.10-alpine sẽ tải xuống image Python 3.10 trên Alpine Linux từ Docker Hub, nó không liên quan đến python version trên máy của mình.
FROM python:3.10-alpine

# WORKDIR /app: Chỉ định thư mục làm việc cho container.
WORKDIR /app

# COPY . .: Sao chép tất cả các file từ thư mục hiện tại vào thư mục /app trong container.\
# Dấu . đầu tiên: đại diện cho toàn bộ files/folders trong context directory trên máy local của bạn
# Dấu . thứ hai: đại diện cho thư mục đích trong container (trong trường hợp này là /app vì đã được set bởi WORKDIR)
# Lệnh này sẽ copy các files từ máy local vào thư mục /app trong container
COPY . .

# RUN pip install -r requirements.txt: Cài đặt tất cả các package được liệt kê trong file requirements.txt.
# RUN pip install -r requirements.txt

# CMD ["python", "example_01.py"]: Chỉ định lệnh sẽ chạy khi container được khởi chạy.
CMD ["python", "example_01.py"]
