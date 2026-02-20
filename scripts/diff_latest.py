#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path


def main() -> int:
    base_dir = Path(__file__).resolve().parent
    out_dir = base_dir / "out"

    if not out_dir.is_dir():
        eprint(f"ディレクトリが見つかりません: {out_dir}")
        return 1

    dirs = (x for x in out_dir.iterdir() if x.is_dir())
    dated_dirs = [x for x in dirs if x.name.isdigit() and len(x.name) == 8]

    if len(dated_dirs) < 2:
        eprint("比較対象のディレクトリが2件未満です")
        return 1

    last, previous = sorted(dated_dirs, key=lambda x: x.name, reverse=True)[:2]

    try:
        result = subprocess.run(
            ["delta", "--paging=never", str(previous), str(last)], check=False
        )
    except FileNotFoundError:
        eprint("`delta` コマンドが見つかりません")
        return 1

    return result.returncode


def eprint(msg):
    print(msg, file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())
