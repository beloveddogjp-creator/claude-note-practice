"""Compare two regular files without changing them. Python 3.9+; no dependencies."""
import argparse
import hashlib
from pathlib import Path
import sys


def digest(path):
    before = path.stat()
    result = hashlib.sha256()
    with path.open('rb') as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b''):
            result.update(chunk)
    after = path.stat()
    signature = lambda s: (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns)
    if signature(before) != signature(after):
        raise ValueError('File changed while being read: ' + str(path))
    return result.hexdigest(), before.st_size


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('original', type=Path)
    parser.add_argument('copy', type=Path)
    args = parser.parse_args()
    try:
        if not args.original.is_file() or not args.copy.is_file():
            raise ValueError('Both paths must be existing regular files.')
        if args.original.samefile(args.copy):
            raise ValueError('Choose two different files, not the same file or a link to it.')
        left, left_size = digest(args.original)
        right, right_size = digest(args.copy)
    except (OSError, ValueError) as error:
        print('ERROR: ' + str(error), file=sys.stderr)
        return 2
    print('Original bytes:', left_size)
    print('Copy bytes:', right_size)
    print('Original SHA-256:', left)
    print('Copy SHA-256:', right)
    if left == right and left_size == right_size:
        print('PASS: the two files have matching SHA-256 and byte counts.')
        return 0
    print('DIFFERENT: keep the original and check the copy process.')
    return 1


if __name__ == '__main__':
    sys.exit(main())
