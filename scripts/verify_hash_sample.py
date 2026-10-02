from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

root = Path(__file__).resolve().parents[1]
folder = root / 'hash-practice'
names = ('README.md', 'compare_files.py', 'sample-original.txt', 'sample-copy.txt')
with zipfile.ZipFile(root / 'file-copy-hash-practice.zip') as package:
    assert sorted(package.namelist()) == sorted('hash-practice/' + n for n in names)
    for name in names:
        assert package.read('hash-practice/' + name) == (folder / name).read_bytes()

def run(left, right, code, message):
    result = subprocess.run([sys.executable, str(folder / 'compare_files.py'), str(left), str(right)], capture_output=True, text=True)
    assert result.returncode == code, result
    assert message in result.stdout + result.stderr, result

run(folder / 'sample-original.txt', folder / 'sample-copy.txt', 0, 'PASS:')
with tempfile.TemporaryDirectory(prefix='lulu-hash-test-') as directory:
    work = Path(directory)
    left, right = work / 'left.txt', work / 'right.txt'
    left.write_bytes(b'abc123')
    right.write_bytes(b'abc124')
    before = [(p.read_bytes(), p.stat().st_size, p.stat().st_mtime_ns) for p in (left, right)]
    run(left, right, 1, 'DIFFERENT:')
    assert [(p.read_bytes(), p.stat().st_size, p.stat().st_mtime_ns) for p in (left, right)] == before
    run(left, work / 'missing.txt', 2, 'ERROR:')
    run(left, left, 2, 'ERROR:')
    alias = work / 'alias.txt'
    alias.symlink_to(left)
    run(left, alias, 2, 'ERROR:')
    hardlink = work / 'hardlink.txt'
    import os
    os.link(left, hardlink)
    run(left, hardlink, 2, 'ERROR:')
    right.write_bytes(left.read_bytes())
    run(left, right, 0, 'PASS:')
print('PASS: ZIP bytes; equal, same-size unequal, missing, same file, symbolic/hard links; no input changes.')
