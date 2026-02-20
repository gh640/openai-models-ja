#!/usr/bin/env python3
from __future__ import annotations

import csv
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


def eprint(msg: str) -> None:
    print(msg, file=sys.stderr)


def fail(msg: str, code: int = 2) -> int:
    eprint(f"ERROR: {msg}")
    return code


def read_csv_rows(path: Path) -> set[tuple[str, str, str]]:
    rows: set[tuple[str, str, str]] = set()
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.add((row["id"], row["owned_by"], row["created"]))
    return rows


def print_ids_block(label: str, ids: list[str]) -> None:
    print(f"REPORT_{label}_IDS_BEGIN")
    for model_id in ids:
        print(model_id)
    print(f"REPORT_{label}_IDS_END")


def main() -> int:
    workspace_arg = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    workspace = workspace_arg.resolve()

    if not workspace.is_dir():
        return fail(f"workspace not found: {workspace_arg}")

    list_models = workspace / "list_models.sh"
    diff_latest = workspace / "scripts" / "diff_latest.py"
    if not list_models.is_file():
        return fail(f"list_models.sh not found in workspace: {workspace}")
    if not diff_latest.is_file():
        return fail(f"scripts/diff_latest.py not found in workspace: {workspace}")
    if not os.getenv("OPENAI_API_KEY"):
        return fail("OPENAI_API_KEY is not set")
    if shutil.which("delta") is None:
        return fail("`delta` command is not installed")

    list_result = subprocess.run([str(list_models)], cwd=workspace)
    if list_result.returncode != 0:
        return list_result.returncode

    out_dir = workspace / "scripts" / "out"
    if not out_dir.is_dir():
        return fail("scripts/out directory not found")

    dated_dirs = sorted(
        [x for x in out_dir.iterdir() if x.is_dir() and re.fullmatch(r"\d{8}", x.name)],
        key=lambda x: x.name,
        reverse=True,
    )
    if len(dated_dirs) < 2:
        return fail("fewer than 2 snapshot directories under scripts/out")

    latest = dated_dirs[0].name
    previous = dated_dirs[1].name
    latest_file = out_dir / latest / "models.csv"
    previous_file = out_dir / previous / "models.csv"
    if not latest_file.is_file() or not previous_file.is_file():
        return fail("snapshot CSV files not found")

    diff_result = subprocess.run([sys.executable, str(diff_latest)], cwd=workspace)
    raw_diff_exit = diff_result.returncode
    if raw_diff_exit not in (0, 1):
        return fail(f"diff_latest.py failed with exit code: {raw_diff_exit}", raw_diff_exit)

    latest_rows = read_csv_rows(latest_file)
    previous_rows = read_csv_rows(previous_file)

    added = sorted(latest_rows - previous_rows)
    removed = sorted(previous_rows - latest_rows)
    diff_status = "changed" if (added or removed) else "unchanged"

    print(f"REPORT_CSV_PATH={latest_file}")
    print(f"REPORT_COMPARE_PREVIOUS={previous}")
    print(f"REPORT_COMPARE_LATEST={latest}")
    print(f"REPORT_DIFF_STATUS={diff_status}")
    print(f"REPORT_ADDED_COUNT={len(added)}")
    print(f"REPORT_REMOVED_COUNT={len(removed)}")

    print_ids_block("ADDED", [x[0] for x in added])
    print_ids_block("REMOVED", [x[0] for x in removed])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
