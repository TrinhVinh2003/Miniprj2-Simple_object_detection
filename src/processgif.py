import cv2
import imageio

def video_to_gif(input_video_path, output_gif_path, fps=10, duration=2):
    cap = cv2.VideoCapture(input_video_path)
    frames = []
    
    # Tính số lượng khung hình tối đa cần cho 2 giây GIF
    max_frames = fps * duration
    frame_count = 0
    
    while cap.isOpened() and frame_count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        # Chuyển đổi màu cho khung hình
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame_rgb)
        frame_count += 1
    
    cap.release()
    
    # Ghi các khung hình thành GIF
    imageio.mimsave(output_gif_path, frames, format="GIF", fps=fps)

# Sử dụng hàm với đường dẫn video đầu vào và tên file GIF đầu ra
video_to_gif("Miniprj2/src/output/output_video.mp4", "Miniprj2/src/output/output_video.gif", fps=10)
