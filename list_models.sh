#!/usr/bin/env zsh
set -eux

PARENT_DIR=$(cd "$(dirname "$0")" >/dev/null 2>&1 && pwd)
DATE="$(date +%Y%m%d)"
DATA_DIR="./scripts/out/${DATE}"
uv run --directory "${PARENT_DIR}" mkdir "${DATA_DIR}"
uv run --directory "${PARENT_DIR}" ./scripts/list_models.py > "${DATA_DIR}/models.csv"
