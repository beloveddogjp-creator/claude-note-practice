"""ファイル一致だけを確認する。Claude Codeの操作は実行しない。"""
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('mode', choices=('edited', 'restored'))
args = parser.parse_args()
root = Path(__file__).resolve().parent
reference = root / ('expected.md' if args.mode == 'edited' else 'draft.before.md')
if not reference.is_file():
    parser.error('比較するファイルがありません: ' + reference.name)
if (root / 'draft.md').read_bytes() != reference.read_bytes():
    parser.exit(1, 'FAIL: draft.mdが' + reference.name + 'と一致しません\n')
print('PASS: draft.md == ' + reference.name)
