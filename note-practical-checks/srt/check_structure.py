from pathlib import Path
import re
import sys

def structure(path):
    text = path.read_text(encoding="utf-8-sig")
    cues = []
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = block.splitlines()
        if len(lines) < 3 or not lines[0].isdigit():
            raise ValueError("invalid cue")
        if not re.fullmatch(r"\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}", lines[1]):
            raise ValueError("invalid timing line")
        cues.append((int(lines[0]), lines[1]))
    if not cues or len({item[0] for item in cues}) != len(cues):
        raise ValueError("empty file or duplicate cue number")
    return cues

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 check_structure.py original.srt edited.srt", file=sys.stderr)
        return 2
    try:
        left, right = map(Path, sys.argv[1:])
        if left.samefile(right):
            raise ValueError("choose two independent files")
        if structure(left) != structure(right):
            print("DIFFERENT: cue count, order, numbers or timing changed.")
            return 1
    except (OSError, UnicodeError, ValueError) as error:
        print("ERROR: " + str(error), file=sys.stderr)
        return 2
    print("PASS: count, order, numbers and times unchanged. Review text meaning and video sync separately.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
