#!/usr/bin/env bash
# Setup for macOS / Linux. Windows users: run setup.ps1 instead.
set -e

# Run from the script's own directory
cd "$(dirname "$0")"

# Create the virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment (.venv)..."
    python3 -m venv .venv
fi

# Deactivate any currently active venv, then activate this one
deactivate 2>/dev/null || true
# shellcheck disable=SC1091
source .venv/bin/activate

# Install certifi and point SSL bundles at it (needed behind the corporate proxy)
pip install --upgrade pip
pip install certifi
export SSL_CERT_FILE="$(python -m certifi)"
export REQUESTS_CA_BUNDLE="$SSL_CERT_FILE"

pip install -r requirements.txt

echo ""
echo "Setup complete."
echo "Activate the environment later with:  source .venv/bin/activate"
