from pathlib import Path
import zipfile

root = Path(__file__).resolve().parents[1]
names = ("CLAUDE.md", "draft.md", "README.md", ".claude/skills/rewrite-japanese/SKILL.md")
with zipfile.ZipFile(root / "claude-note-practice.zip") as archive:
    assert sorted(archive.namelist()) == sorted("claude-note-practice/" + n for n in names)
    for name in names:
        data = (root / name).read_bytes()
        data.decode("utf-8")
        assert archive.read("claude-note-practice/" + name) == data
skill = (root / names[-1]).read_text(encoding="utf-8")
assert skill.startswith("---\nname: rewrite-japanese\ndescription: ")
assert "LULU-AI-Knowledge" not in (root / "README.md").read_text(encoding="utf-8")
print("PASS: four UTF-8 sample files and ZIP match. Claude execution is not tested.")
