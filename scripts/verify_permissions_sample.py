from pathlib import Path
import json,zipfile
root=Path(__file__).resolve().parents[1]
p=root/"permission-practice"
config=json.loads((p/"settings.example.json").read_text())
assert config=={"permissions":{"defaultMode":"default","ask":["Edit","Bash"]}}
names=("README.md","draft.md","settings.example.json",".gitignore")
with zipfile.ZipFile(root/"claude-permission-practice.zip") as z:
    assert sorted(z.namelist())==sorted("claude-permission-practice/"+n for n in names)
    for n in names:
        data=(p/n).read_bytes();data.decode("utf-8")
        assert z.read("claude-permission-practice/"+n)==data
assert not (p/".claude/settings.local.json").exists()
assert (p/".gitignore").read_text()==".claude/settings.local.json\n"
print("PASS: inert JSON example and four-file ZIP match. Claude runtime behavior is not tested.")
