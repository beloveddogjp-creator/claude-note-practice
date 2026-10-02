"""Read-only input checks. Does not call Premiere, AI services, or billing APIs."""
from pathlib import Path
import argparse
import csv
import sys

FIELDS = ['model', 'resolution', 'aspect_ratio', 'frame_rate', 'duration',
          'estimated_credits', 'actual_usage', 'reference_frames', 'audio', 'review_result']

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--folder', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    try:
        folder = args.folder
        prompt = (folder / 'video-prompt.txt').read_text(encoding='utf-8').strip()
        checklist = (folder / 'review-checklist.md').read_text(encoding='utf-8').strip()
        with (folder / 'settings-record.csv').open(encoding='utf-8', newline='') as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != FIELDS:
                raise ValueError('record columns do not match')
            rows = list(reader)
        if not prompt or not checklist or not rows:
            raise ValueError('empty input file')
        if any(None in row or any(value is None for value in row.values()) for row in rows):
            raise ValueError('incomplete record row')
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        print('ERROR:', error, file=sys.stderr)
        return 2
    print('PASS: input files ready; no Premiere generation executed.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
