# Tail Database R2 Uploader

Uploads data that has been exported by [tail-database-exporter](https://github.com/Tail-Database/tail-database-exporter) to [Cloudflare R2](https://www.cloudflare.com/en-gb/products/r2/).

## How to run

### Install dependencies

```bash
python3 -m venv venv
. ./venv/bin/activate
python3 setup.py install
```

### Run the script

```bash
python3 start.py
```
