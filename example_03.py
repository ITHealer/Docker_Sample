from flask import Flask
import mysql.connector

app = Flask(__name__)


@app.route('/')
def hello():
    # MySQL param
    MYSQL_HOST = 'mysql'
    MYSQL_DB = 'mysql'
    MYSQL_USER = 'root'
    MYSQL_PASS = 'password'
    rowcount = -1
    connection = None
    try:
        connection = mysql.connector.connect(host=MYSQL_HOST, database=MYSQL_DB, user=MYSQL_USER,
                                             password=MYSQL_PASS, port=3306, auth_plugin='mysql_native_password')
        mysql_insert_query = "SELECT * FROM mysql.user"
        print(mysql_insert_query)
        cursor = connection.cursor()
        cursor.execute(mysql_insert_query)
        records = cursor.fetchall()
        rowcount = cursor.rowcount

    except mysql.connector.Error as error:
        print("Fail login {}".format(error))
        ret_result = -1
    finally:
        if connection is not None:
            connection.close()
        del connection

    return "Total user numers = : "+  str(rowcount)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000', use_reloader=False)


# """
# Chạy MySQL container:
#     docker run -d --name mysql-container --net <name_network> -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql:latest

# Chạy Flask app container:
#     docker run -d --name flask-app --net <name_network> -p 5000:5000 flask-app:latest

# # Cấu hình mysql để cho phép kết nối từ bên ngoài vào container mysql. Vì user root mặc định chỉ cho phép kết nối từ localhost.
# Truy cập bash trong container Flask:
#     docker exec -it flask-app bash: mục đích là vào bash của container Flask để chạy các lệnh MySQL giúp cấu hình user and database.
#     mysql -u root -p
#     update mysql.user set host = '%' where user = 'root';
#     ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
#     FLUSH PRIVILEGES;
#     show databases;
#     use mysql;
#     show tables;
#     select * from user;
#     exit;
# docker run --name example_03 -p 8888:5000 --net example_conn2container example_03

#     - docker run --name example_03 -p 8080:5000 healer/images_example_03 

# Các lệnh MySQL để cấu hình user:
# Giải thích:
#     --net <name_network>: Kết nối container vào network tên "<name_network>"
#     -p 3306:3306: Map port 3306 từ container ra host
#     -e MYSQL_ROOT_PASSWORD=root: Set password cho root user
#     -d: Chạy container ở chế độ detached (background)
#     -it: Cho phép tương tác với terminal
#     --rm: Tự động xóa container khi exit

# Các lệnh MySQL dùng để:
#     + Cho phép root user connect từ bất kỳ host nào (%)
#     + Đổi authentication method sang mysql_native_password
#     + Refresh privileges
# """