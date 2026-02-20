---
name: fetch-list-and-report-changes
description: Fetch the latest OpenAI model list into CSV and report changes from the previous snapshot in repositories that use `list_models.sh` and `scripts/diff_latest.py`. Use when the user asks to refresh model snapshots, compare with the last run, or summarize added/removed model IDs.
---

# Fetch List And Report Changes

## Overview

Execute a fixed workflow for model snapshot refresh and diff reporting.
Prefer the bundled script for deterministic output.

## Workflow

1. Confirm the workspace has both `list_models.sh` and `scripts/diff_latest.py`.
2. Run `python3 scripts/fetch_and_report.py <workspace>` from this skill directory, or run `python3 scripts/fetch_and_report.py .` when already in the target workspace.
3. Read and relay:
   - generated CSV path
   - compared snapshot dates
   - changed/unchanged status
   - added/removed counts
   - added/removed model IDs (if any)
4. If the script fails due to missing key or missing tools, report the concrete blocker and stop.

## Commands

Run from anywhere:

```bash
python3 .agents/skills/fetch-list-and-report-changes/scripts/fetch_and_report.py /path/to/repo
```

Run from target repository root:

```bash
python3 .agents/skills/fetch-list-and-report-changes/scripts/fetch_and_report.py .
```

## Notes

- Require `OPENAI_API_KEY` for `list_models.sh`.
