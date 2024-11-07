# Mini project: Vehicle Detection and Counting

ự án này phát hiện, đếm và theo dõi các phương tiện trong video, đặc biệt tập trung vào các phương tiện trong các làn đường riêng biệt và đếm chúng khi chúng đi qua một khu vực cụ thể. Thư viện OpenCV được sử dụng để xử lý hình ảnh và phát hiện đường viền, cùng với logic tùy chỉnh để theo dõi các đối tượng và tránh đếm trùng lặp. Dự án này không sử dụng mô hình deep learning để nhận diện và theo dõi đối tượng nên độ chính xác có thể chưa cao và cần cải tiến thêm trong tương lai. Video đã xử lý được lưu dưới dạng tệp đầu ra với định dạng .mp4.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#features)
- [Configuration](#configuration)
- [Example Output](#example-output)

## Installation
### Requirements

- **Python 3.x**
- **OpenCV**
- **Numpy**
### Clone the Repository
Clone the repository to your local machine:
```bash
   git Clone    
    cd vehicle-detection
```
## Usage
1. Chuẩn bị video: Đặt video đầu vào vào thư mục video/ và cập nhật đường dẫn vào trong code nếu cần thiết.
2. Chạy chương trình: Chạy file main.py để bắt đầu quá trình phát hiện xe và lưu video đầu ra:

3. Video đầu ra: video đã được xử lý sẽ được lưu trong đường dẫn `output/output_video.mp4`.

## Project Structure
```
vehicle-detection-tracking/
│
├── config.py                 # Tệp cấu hình cho các tham số và đường dẫn
├── detector.py               # Logic phát hiện xe
├── tracker.py                # Logic theo dõi xe
├── utils.py                  # Các hàm tiện ích để xử lý video
├── video/                    # Thư mục chứa các video đầu vào
│   └── input_video.mp4       # Ví dụ video đầu vào
└── output/                   # Thư mục lưu video đã xử lý
    └── output_video.mp4      # Video đầu ra đã xử lý
```

### Video demo
![Vehicle Detection Demo](output/video.gif)
