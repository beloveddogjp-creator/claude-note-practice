from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / 'note-practical-checks'
files = sorted(p for p in BUNDLE.rglob('*') if p.is_file())
with zipfile.ZipFile(ROOT / 'note-practical-checks.zip') as archive:
    assert sorted(archive.namelist()) == sorted(p.relative_to(ROOT).as_posix() for p in files)
    for path in files:
        assert archive.read(path.relative_to(ROOT).as_posix()) == path.read_bytes()
summary = json.loads((BUNDLE / 'verification-summary.json').read_text())
assert summary['srt']['actual_ai_run'] is False
assert summary['practice']['human_learning_effect_measured'] is False
assert summary['srt']['timings_and_order_preserved']
assert all(summary['srt']['rejected'].values())
assert hashlib.sha256((BUNDLE / 'ffmpeg/synthetic-qc-8s.mp4').read_bytes()).hexdigest() == summary['ffmpeg_qc']['input_sha256_unchanged']
for path in [BUNDLE / 'ffmpeg/synthetic-qc-8s.mp4', BUNDLE / 'practice/source-4s.mp4']:
    assert path.read_bytes()[4:8] == b'ftyp'

checker = BUNDLE / 'srt/check_structure.py'
original = BUNDLE / 'srt/original.srt'
edited = BUNDLE / 'srt/edited-example.srt'

def run(left, right, expected_code):
    before = [(p, p.read_bytes(), p.stat().st_mtime_ns) for p in (left, right) if p.exists()]
    result = subprocess.run([sys.executable, str(checker), str(left), str(right)], capture_output=True, text=True)
    assert result.returncode == expected_code, result.stdout + result.stderr
    assert all(p.read_bytes() == data and p.stat().st_mtime_ns == timestamp for p, data, timestamp in before)

run(original, edited, 0)
run(original, original, 2)
with tempfile.TemporaryDirectory(prefix='lulu-srt-check-') as directory:
    work = Path(directory)
    data = edited.read_text()
    variants = {
        'time': data.replace('00:00:01,000', '00:00:01,100', 1),
        'delete': '\n\n'.join(data.strip().split('\n\n')[:-1]) + '\n',
        'order': '\n\n'.join(reversed(data.strip().split('\n\n'))) + '\n',
        'duplicate': data + '\n' + data.strip().split('\n\n')[0] + '\n',
        'semantic': data.replace('こちらの設定を確認してください。', '確認は不要です。'),
    }
    for name, text in variants.items():
        path = work / (name + '.srt')
        path.write_text(text, encoding='utf-8')
        run(original, path, 0 if name == 'semantic' else 2 if name == 'duplicate' else 1)
    run(original, work / 'missing.srt', 2)
print('PASS: ZIP bytes, synthetic media hash, SRT timing/deletion/order/duplicate/missing/same-file cases, read-only behavior; semantic limit retained.')
