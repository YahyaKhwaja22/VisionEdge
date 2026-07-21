from ultralytics import YOLO
import cv2
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

video_path = ROOT / "assets" / "videos" / "traffic.mp4"

output_path = ROOT / "assets" / "videos" / "output.mp4"

model = YOLO("yolo11n.pt")

cap = cv2.VideoCapture(str(video_path))

if not cap.isOpened():
    print("Error opening video.")
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter(
    str(output_path),
    fourcc,
    fps,
    (width, height)
)

frame_count = 0
start_time = time.time()

while True:

    success, frame = cap.read()

    if not success:
        break

    results = model(frame)

    annotated = results[0].plot()

    writer.write(annotated)

    frame_count += 1

cap.release()
writer.release()

elapsed = time.time() - start_time

print("-----------------------------------")
print("Video Completed")
print("-----------------------------------")
print(f"Frames : {frame_count}")
print(f"Time   : {elapsed:.2f} sec")
print(f"FPS    : {frame_count/elapsed:.2f}")