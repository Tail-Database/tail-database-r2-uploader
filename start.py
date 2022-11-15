import boto3
from config import Config

s3 = boto3.resource('s3',
  endpoint_url = f"https://{Config.cloudflare_account_id}.r2.cloudflarestorage.com",
  aws_access_key_id = Config.cloudflare_access_key_id,
  aws_secret_access_key = Config.cloudflare_secret_access_key,
)
