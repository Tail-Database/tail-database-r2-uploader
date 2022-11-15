import glob
import os
import boto3

from config import Config

if Config.cloudflare_account_id is None:
    raise Exception("CLOUDFLARE_ACCOUNT_ID must be set")

if Config.cloudflare_access_key_id is None:
    raise Exception("CLOUDFLARE_ACCESS_KEY_ID must be set")

if Config.cloudflare_secret_access_key is None:
    raise Exception("CLOUDFLARE_SECRET_ACCESS_KEY must be set")

if Config.input_directory is None:
    raise Exception("R2_UPLOADER_INPUT_DIR must be set")

if Config.environment is None:
    raise Exception("R2_UPLOADER_ENVIRONMENT must be set")

s3 = boto3.client('s3',
  endpoint_url = f"https://{Config.cloudflare_account_id}.r2.cloudflarestorage.com",
  aws_access_key_id = Config.cloudflare_access_key_id,
  aws_secret_access_key = Config.cloudflare_secret_access_key,
)

bucket_name = f"tail-database-tails-{Config.environment}"

for filename in glob.glob(f"{Config.input_directory}/*.json"):
    key = os.path.basename(filename)

    s3.upload_file(filename, bucket_name, key)

    print(f"Uploaded {key} to {bucket_name}")
