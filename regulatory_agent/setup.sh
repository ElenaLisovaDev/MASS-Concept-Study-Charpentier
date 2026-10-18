deactivate
source .venv/bin/activate
pip install certifi
export SSL_CERT_FILE=$(python -m certifi)
export REQUESTS_CA_BUNDLE=$(python -m certifi)
pip install -r requirements.txt
