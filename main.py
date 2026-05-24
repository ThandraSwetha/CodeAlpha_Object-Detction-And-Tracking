from ultralytics import YOLO
import cv2

model = YOLO("yolov8s.pt")

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        break

    # Detect only selected classes
    results = model.track(
        frame,
        persist=True,
        classes=[0, 39, 67, 63],
        conf=0.5
    )

    annotated_frame = results[0].plot()

    cv2.imshow("Tracking", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()