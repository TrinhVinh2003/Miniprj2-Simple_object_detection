import cv2
import imageio

def video_to_gif(input_video_path, output_gif_path, fps=10):
    cap = cv2.VideoCapture(input_video_path)
    frames = []
    
    # Đọc từng khung hình và thêm vào danh sách frames
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Chuyển đổi màu cho khung hình
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame_rgb)
    
    cap.release()
    
    # Ghi các khung hình thành GIF
    imageio.mimsave(output_gif_path, frames, format="GIF", fps=fps)

# Sử dụng hàm với đường dẫn video đầu vào và tên file GIF đầu ra
video_to_gif("Miniprj2/src/output/output_video.mp4", "Miniprj2/src/output/output_video.gif", fps=10)
