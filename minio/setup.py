# Créer les buckets
# Créer les utilisateurs avec les accès aux buckets

buckets_to_create = [
    "raw", 
    "staging",
    "curated", 
    "archived"
]

import boto3
import os

access_key_id = os.environ["MINIO_ROOT_USER"]
secret_access_key = os.environ["MINIO_ROOT_PASSWORD"]
minio_endpoint = os.environ["MINIO_ENDPOINT"]

# https://docs.aws.amazon.com/boto3/latest/reference/services/s3.html

s3 = boto3.client(
    's3',
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    endpoint_url=minio_endpoint,
)

for bucket in buckets_to_create :
    s3.create_bucket(
        ACL="private",
        Bucket=bucket
    )
    print(f"Created Bucket '{minio_endpoint}{bucket}'")
