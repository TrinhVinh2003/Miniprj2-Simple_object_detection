import math
import config
import cv2
class VehicleTracker:
    cap = cv2.VideoCapture(config.VIDEO_PATH)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    def __init__(self, frame_countdown, max_distance):
        self.vehicle_tracks = {}
        self.next_vehicle_id = 0
        self.frame_countdown = frame_countdown
        self.max_distance = max_distance
    def update_tracks(self, detected_centroids,width):
        left_lane_count = 0
        right_lane_count = 0

        for cx, cy, x, y, w, h in detected_centroids:
            matched = False
            for vehicle_id, (prev_cx, prev_cy, countdown) in list(
                self.vehicle_tracks.items()
            ):
                if math.dist((cx, cy), (prev_cx, prev_cy)) < self.max_distance:
                    self.vehicle_tracks[vehicle_id] = (cx, cy, self.frame_countdown)
                    matched = True
                    if cx < width // 2:
                        left_lane_count += 1
                    else:
                        right_lane_count += 1
                    break

            if not matched:
                self.vehicle_tracks[self.next_vehicle_id] = (
                    cx,
                    cy,
                    self.frame_countdown,
                )
                self.next_vehicle_id += 1

        # Giảm countdown của các xe không còn trong khung và loại bỏ xe đã ra khỏi vùng giới hạn
        for vehicle_id, data in list(self.vehicle_tracks.items()):
            cx, cy, countdown = data
            if countdown > 0:
                self.vehicle_tracks[vehicle_id] = (cx, cy, countdown - 1)
            else:
                del self.vehicle_tracks[vehicle_id]
        return left_lane_count, right_lane_count