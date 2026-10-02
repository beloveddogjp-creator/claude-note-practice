"""自作の練習素材だけを生成。既存出力があれば上書きしない。"""
from pathlib import Path
import math
import struct
import subprocess
import wave

folder = Path(__file__).resolve().parents[1] / 'media-practice'
assert not (folder / 'sample.mp4').exists()
assert not (folder / 'channels.wav').exists()
rate = 24000
with wave.open(str(folder / 'channels.wav'), 'wb') as out:
    out.setnchannels(2)
    out.setsampwidth(2)
    out.setframerate(rate)
    frames = bytearray()
    for n in range(rate * 3):
        left = round(3000 * math.sin(2 * math.pi * 440 * n / rate))
        right = round(3000 * math.sin(2 * math.pi * 660 * n / rate))
        frames.extend(struct.pack('<hh', left, right))
    out.writeframes(frames)
subprocess.run(['ffmpeg', '-v', 'error', '-n', '-f', 'lavfi', '-i',
                'testsrc2=size=640x360:rate=30:duration=3',
                '-i', str(folder / 'channels.wav'), '-c:v', 'libx264', '-crf', '28',
                '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '96k', '-shortest',
                str(folder / 'sample.mp4')], check=True)
print('Created synthetic video and stereo tones only.')
