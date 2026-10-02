from pathlib import Path
import argparse
import json
import re
import subprocess
import sys
import wave
import zipfile

parser = argparse.ArgumentParser()
parser.add_argument('--decode', action='store_true')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
folder = root / 'media-practice'
names = ('README.md', 'sample.mp4', 'channels.wav', 'sample.srt', 'probe.py')
with zipfile.ZipFile(root / 'video-media-practice.zip') as package:
    assert sorted(package.namelist()) == sorted('media-practice/' + n for n in names)
    for name in names:
        assert package.read('media-practice/' + name) == (folder / name).read_bytes()
with wave.open(str(folder / 'channels.wav')) as audio:
    assert (audio.getnchannels(), audio.getsampwidth(), audio.getframerate(), audio.getnframes()) == (2, 2, 24000, 72000)
assert len(re.findall(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', (folder / 'sample.srt').read_text())) == 2
if args.decode:
    result = subprocess.run([sys.executable, str(folder / 'probe.py'), str(folder / 'sample.mp4')], capture_output=True, text=True, check=True)
    info = json.loads(result.stdout)
    video = next(s for s in info['streams'] if s['codec_type'] == 'video')
    audio = next(s for s in info['streams'] if s['codec_type'] == 'audio')
    assert (video['codec_name'], video['width'], video['height'], video['r_frame_rate'], video['avg_frame_rate']) == ('h264', 640, 360, '30/1', '30/1')
    assert (audio['codec_name'], audio['channels'], audio['sample_rate']) == ('aac', 2, '24000')
    assert abs(float(info['format']['duration']) - 3) < 0.01
    subprocess.run(['ffmpeg', '-v', 'error', '-i', str(folder / 'sample.mp4'), '-f', 'null', '-'], check=True)
    missing = subprocess.run([sys.executable, str(folder / 'probe.py'), str(folder / 'missing.mp4')], capture_output=True)
    assert missing.returncode == 1
    print(json.dumps(info, indent=2))
print('PASS: ZIP, WAV header and SRT. Decode check=' + str(args.decode) + '. Premiere/subjective playback not tested.')
