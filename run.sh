#!/usr/bin/env bash

cd /root/tail-database-r2-uploader
/usr/bin/python3 -m venv venv
. ./venv/bin/activate
python3 -u setup.py install

R2_UPLOADER_INPUT_DIR=/root/.tail-database-exporter/mainnet R2_UPLOADER_ENVIRONMENT=mainnet python3 -u start.py
