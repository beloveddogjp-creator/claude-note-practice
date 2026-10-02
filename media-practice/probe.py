"""ffprobeで実体の映像・音声情報を読む。素材は変更しない。"""
import argparse
import json
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument('file')
args = parser.parse_args()
command = ['ffprobe', '-v', 'error', '-show_entries',
           'stream=codec_type,codec_name,width,height,r_frame_rate,avg_frame_rate,channels,sample_rate:format=format_name,duration',
           '-of', 'json', args.file]
try:
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    info = json.loads(result.stdout)
except FileNotFoundError:
    parser.exit(2, 'ffprobeが見つかりません。既に導入済みの環境で試してください。\n')
except (subprocess.CalledProcessError, json.JSONDecodeError) as error:
    parser.exit(1, '読み取りに失敗しました: ' + str(error) + '\n')
json.dump(info, sys.stdout, ensure_ascii=False, indent=2)
print()
