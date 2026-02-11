#!/usr/bin/env zsh
set -eux

PARENT_DIR=$(cd "$(dirname "$0")" >/dev/null 2>&1 && pwd)
DATE="${DATE:-$(date +%Y%m%d)}"
DATA_DIR="${PARENT_DIR}/scripts/out/${DATE}"
mkdir -p "${DATA_DIR}"
uv run --directory "${PARENT_DIR}" ./scripts/list_models.py > "${DATA_DIR}/models.csv"
