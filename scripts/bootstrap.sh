#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_PATH="${ROOT_DIR}/.venv"
PYTHON_BIN="${PYTHON:-python3}"

if ! command -v "${PYTHON_BIN}" >/dev/null 2>&1; then
  echo "[bootstrap] Python interpreter '${PYTHON_BIN}' not found" >&2
  exit 1
fi

echo "[bootstrap] Creating virtual environment at ${VENV_PATH}"
"${PYTHON_BIN}" -m venv "${VENV_PATH}"

# shellcheck disable=SC1091
source "${VENV_PATH}/bin/activate"

echo "[bootstrap] Upgrading pip"
python -m pip install --upgrade pip

echo "[bootstrap] Installing TONPROBE and development dependencies"
pip install -e "${ROOT_DIR}[dev]"

echo "[bootstrap] Setup complete. Activate with: source ${VENV_PATH}/bin/activate"
