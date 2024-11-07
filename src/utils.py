import cv2
import numpy as np
import os

import config  # Đảm bảo file config có chứa giá trị line_position

def process_video(video_path, detector, tracker):
    # Kiểm tra và tạo thư mục output nếu chưa tồn tại
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Cấu hình ghi video đầu ra
    output_path = os.path.join(output_dir, "output_video.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Thử với codec mp4v
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    if not out.isOpened():
        print("Không thể mở VideoWriter. Kiểm tra codec và đường dẫn.")
        return

    if cap.isOpened():
        ret, frame1 = cap.read()
    else:
        ret = False

    ret, frame2 = cap.read()
    while ret:
        # Xử lý hình ảnh
        d = cv2.absdiff(frame1, frame2)
        grey = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(grey, (3, 3), 0)
        _, th = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(th, np.ones((4, 4)), iterations=2)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
        opening = cv2.morphologyEx(dilated, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

        # Vẽ đường line
        cv2.line(frame1, (0, height // 2), (width, height // 2), (255, 255, 0), 2)
        cv2.line(frame1, (0, config.line_position), (width, config.line_position), (0, 255, 0), 2)

        # Phát hiện và đếm xe
        detected_centroids = detector.detect_vehicle(frame1, closing)
        left_count, right_count = tracker.update_tracks(detected_centroids, width)

        # Hiển thị đếm số lượng
        display_counts(frame=frame1, left_count=left_count, right_count=right_count)
        out.write(frame1)  # Lưu frame vào file đầu ra
        cv2.imshow("Vehicle Detection", frame1)

        if cv2.waitKey(40) & 0xFF == ord("q"):
            break

        frame1 = frame2
        ret, frame2 = cap.read()

    cap.release()
    out.release()  # Giải phóng đối tượng ghi file
    cv2.destroyAllWindows()

def display_counts(frame, left_count, right_count):
    text = f"Left: {left_count} | Right: {right_count}"
    cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (64, 50, 168), 2)
