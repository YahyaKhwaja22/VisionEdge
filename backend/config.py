from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

VIDEO_PATH = ROOT / "assets" / "videos" / "traffic.mp4"

OUTPUT_VIDEO = ROOT / "assets" / "videos" / "output.mp4"

MODEL = ROOT / "models" / "yolo11n.pt"