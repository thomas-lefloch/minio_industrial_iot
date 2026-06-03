# Ajout de fichier dans le bucket raw/ par lignes de production
# TODO: Check de l'intégrité des fichiers md5

import time

timestamp = int(time.time())

# la clé est séparé par ligne de production.
# Un timestamp suivi d'un suffixe permet l'ajout de plusieurs fichiers au même moment
files_to_upload = [
    {
        "filepath": "source_dataset/LineA_Stable_10K.csv",
        "key": f"production_line/line_a/{timestamp}_0.csv",
    },
    {
        "filepath": "source_dataset/LineB_Flux.csv",
        "key": f"production_line/line_b/{timestamp}_0.csv",
    },
    {
        "filepath": "source_dataset/LineC_Turbulent.csv",
        "key": f"production_line/line_c/{timestamp}_0.csv",
    },
    {
        "filepath": "source_dataset/LineD_SpikeControl.csv",
        "key": f"production_line/line_d/{timestamp}_0.csv",
    },
    {
        "filepath": "source_dataset/LineE_SmoothRun.csv",
        "key": f"production_line/line_e/{timestamp}_0.csv",
    },
]

import hashlib
import base64
import boto3
import os

# FIXME do not use root account. use acocunt created for pipeline
access_key_id = os.environ["MINIO_ROOT_USER"]
secret_access_key = os.environ["MINIO_ROOT_PASSWORD"]
minio_endpoint = os.environ["MINIO_ENDPOINT"]

s3 = boto3.client(
    "s3",
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    endpoint_url=minio_endpoint,
)

for file in files_to_upload:
    
    with open(file["filepath"], "rb") as f:
        file_content = f.read()
    expected_md5 = base64.b64encode(hashlib.md5(file_content).digest()).decode()

    # Can't seem to check md5 integrity with upload_file() ChecksumMD5 seems to be ignored
    # response = s3.upload_file(
    #     file["filepath"],
    #     "raw",
    #     file["key"],
    #     ExtraArgs={"ChecksumAlgorithm": "MD5", "ChecksumMD5": expected_md5}
    # )
    
    try:
        response = s3.put_object(
            Body=file_content,
            Bucket="raw",
            Key=file["key"],
            ContentMD5=expected_md5,
        )
    except Exception as err:
        print("Failed to upload", file["filepath"], ": Integrity check failed !")
        continue

    print(file["filepath"], "uploaded as", file["key"], "on bucket 'raw'")
