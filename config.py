import os

class Config:
    cloudflare_account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID", None)
    cloudflare_access_key_id = os.getenv("CLOUDFLARE_ACCESS_KEY_ID", None)
    cloudflare_secret_access_key = os.getenv("CLOUDFLARE_SECRET_ACCESS_KEY", None)
    input_directory = os.getenv("R2_UPLOADER_INPUT_DIR", None)
