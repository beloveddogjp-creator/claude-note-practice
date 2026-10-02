from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

root = Path(__file__).resolve().parents[1]
sample = root / 'rewind-practice'
names = ('README.md', 'draft.md', 'expected.md', 'check_files.py', '.gitignore')
with zipfile.ZipFile(root / 'claude-rewind-practice.zip') as package:
    assert sorted(package.namelist()) == sorted('rewind-practice/' + n for n in names)
    for name in names:
        assert package.read('rewind-practice/' + name) == (sample / name).read_bytes()
assert (sample / 'expected.md').read_text() == (sample / 'draft.md').read_text().replace('作業を行う', '作業をする')
with tempfile.TemporaryDirectory() as target:
    folder = Path(target)
    for name in names:
        (folder / name).write_bytes((sample / name).read_bytes())
    (folder / 'draft.before.md').write_bytes((folder / 'draft.md').read_bytes())
    def check(mode, code):
        result = subprocess.run([sys.executable, str(folder / 'check_files.py'), mode], capture_output=True, text=True)
        assert result.returncode == code, result
    check('restored', 0)
    check('edited', 1)
    (folder / 'draft.md').write_bytes((folder / 'expected.md').read_bytes())
    check('edited', 0)
    check('restored', 1)
print('PASS: ZIP and file comparison positive/negative cases. Claude interactive execution not tested.')
