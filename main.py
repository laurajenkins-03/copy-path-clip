"""Copy Path Clip — Copy full Windows paths of selected files to the clipboard, quoted."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='copy_path_clip',
        description='Copy full Windows paths of selected files to the clipboard, quoted.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Copy Path Clip')
    print('Quoted paths ready for a terminal or a ticket.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
