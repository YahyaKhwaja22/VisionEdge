from ultralytics import YOLO
import cv2

from config import *

from decoder.video_reader import VideoReader

from renderer.draw import Renderer

from telemetry.fps import FPSCounter

reader = VideoReader(str(VIDEO_PATH))

model = YOLO(str(MODEL))

fps_counter = FPSCounter()

width = int(reader.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(reader.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = reader.cap.get(cv2.CAP_PROP_FPS)

writer = cv2.VideoWriter(
    str(OUTPUT_VIDEO),
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height),
)

while True:

    success, frame = reader.read()

    if not success:

        break

    results = model(frame)

    image = Renderer.draw(results)

    writer.write(image)

    fps_counter.update()

reader.release()

writer.release()

print("--------------------------------")

print("Processing Complete")

print(f"Average FPS : {fps_counter.fps():.2f}")

print("--------------------------------")