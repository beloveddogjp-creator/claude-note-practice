from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

root = Path(__file__).resolve().parents[1]
folder = root / 'premiere-generative-practice'
names = ('README.md', 'video-prompt.txt', 'settings-record.csv', 'review-checklist.md', 'check_sample.py')
with zipfile.ZipFile(root / 'premiere-generative-practice.zip') as package:
    assert sorted(package.namelist()) == sorted('premiere-generative-practice/' + n for n in names)
    for name in names:
        assert package.read('premiere-generative-practice/' + name) == (folder / name).read_bytes()

def run(target, code, message):
    result = subprocess.run([sys.executable, str(folder / 'check_sample.py'), '--folder', str(target)], capture_output=True, text=True)
    assert result.returncode == code, result
    assert message in result.stdout + result.stderr, result

before = [(p.name, p.read_bytes(), p.stat().st_mtime_ns) for p in folder.iterdir() if p.is_file()]
run(folder, 0, 'PASS: input files ready; no Premiere generation executed.')
after = [(p.name, p.read_bytes(), p.stat().st_mtime_ns) for p in folder.iterdir() if p.is_file()]
assert before == after
with tempfile.TemporaryDirectory(prefix='lulu-generation-input-test-') as directory:
    test = Path(directory)
    for name in names:
        (test / name).write_bytes((folder / name).read_bytes())
    (test / 'settings-record.csv').write_text('wrong\nvalue\n', encoding='utf-8')
    run(test, 2, 'record columns do not match')
    (test / 'settings-record.csv').write_bytes((folder / 'settings-record.csv').read_bytes())
    (test / 'video-prompt.txt').write_text('', encoding='utf-8')
    run(test, 2, 'empty input file')
    run(test / 'missing', 2, 'ERROR:')
print('PASS: ZIP matches; valid, wrong columns, empty, missing; input files unchanged. Generation untested.')
