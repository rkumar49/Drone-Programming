# test_mediapipe.py
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

print("✅ MediaPipe imported correctly")
print(f"Version: {mp.__version__}")
print("Available modules:", dir(mp))