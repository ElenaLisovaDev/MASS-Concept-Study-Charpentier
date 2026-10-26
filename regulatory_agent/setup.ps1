# Setup for Windows (PowerShell). macOS/Linux users: run setup.sh instead.
$ErrorActionPreference = 'Stop'

# Run from the script's own directory
Set-Location -Path $PSScriptRoot

# Create the virtual environment if it doesn't exist
if (-not (Test-Path ".venv")) {
    Write-Output "Creating virtual environment (.venv)..."
    python -m venv .venv
}

# Activate it
& .\.venv\Scripts\Activate.ps1

# Install certifi and point SSL bundles at it (needed behind the corporate proxy)
python -m pip install --upgrade pip
pip install certifi
$env:SSL_CERT_FILE = (python -m certifi)
$env:REQUESTS_CA_BUNDLE = $env:SSL_CERT_FILE

pip install -r requirements.txt

Write-Output ""
Write-Output "Setup complete."
Write-Output "Activate the environment later with:  .\.venv\Scripts\Activate.ps1"
