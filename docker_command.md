
## Khi bạn pull một image từ Docker Hub về, image đó sẽ được lưu trữ trên máy local của bạn
- Đường dẫn mặc định lưu Docker images trên máy local là:
    C:\Users\<username>\AppData\Local\Docker\wsl\data\ext4\docker-desktop-data\data\docker\volumes\docker_desktop_data_root


### Để kiểm tra dung lượng Docker đang sử dụng:
    docker system df

### Để xóa images không sử dụng để giải phóng bộ nhớ:
    docker image prune

### Để xóa một image cụ thể:
    docker rmi image_name
     

Để xóa image này, bạn cần thực hiện theo 2 bước:
1. Xóa container đã sử dụng image đó:
    docker rm container_name
2. Xóa image đó:
    docker rmi image_name


Hoặc bạn có thể dùng flag `-f` (force) để xóa cả image và container cùng lúc:
    docker rm -f container_name
    docker rmi -f image_name


Để xem danh sách tất cả các containers (kể cả đã dừng), bạn có thể dùng:
    docker ps -a

Để xem danh sách tất cả các images, bạn có thể dùng:
    docker images

Để xem danh sách tất cả các volumes, bạn có thể dùng:
    docker volume ls

Để xem danh sách tất cả các networks, bạn có thể dùng:
    docker network ls

Để xem danh sách tất cả các images và containers, bạn có thể dùng:
    docker ps -a
    docker images

Để xem thông tin chi tiết về một container, bạn có thể dùng:
    docker inspect container_name

Để xem thông tin chi tiết về một image, bạn có thể dùng:
    docker inspect image_name

Để xem thông tin chi tiết về một volume, bạn có thể dùng:
    docker volume inspect volume_name

Để xem thông tin chi tiết về một network, bạn có thể dùng:
    docker network inspect network_name











