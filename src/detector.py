import cv2
class VehicleDetector:

    def __init__(self, min_contour_width, min_contour_height, min_area, max_area, line_position):
        self.min_contour_width = min_contour_width
        self.min_contour_height = min_contour_height
        self.min_area = min_area
        self.max_area = max_area
        self.line_position = line_position
    def detect_vehicle(self, frame, fgmask):
        contours, h = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        vehicles = []
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            area = cv2.contourArea(contour)
            contour_valid = (w >= self.min_contour_width) and (h >= self.min_contour_height)
            if self.min_area < area < self.max_area and contour_valid:
                M = cv2.moments(contour)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                if frame.shape[0] // 2 < cy:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    if cy < self.line_position:
                        # Cập nhật danh sách centroid mới
                        vehicles.append((cx, cy, x, y, w, h))
                else:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return vehicles