from pathlib import Path

import boto3
from botocore.config import Config
from botocore.exceptions import BotoCoreError, ClientError

ENDPOINT = "http://localhost:4566"
BUCKET = "documente-demo"
OBJECT_KEY = "document.txt"

PROJECT_DIR = Path(__file__).resolve().parent
ORIGINAL = PROJECT_DIR / "document.txt"
DOWNLOADED = PROJECT_DIR / "document-descarcat.txt"


def main():
    # Toate cererile sunt trimise către emulatorul local.
    # Credențialele sunt fictive, folosite exclusiv pentru demonstrație.
    s3 = boto3.client(
        "s3",
        endpoint_url=ENDPOINT,
        aws_access_key_id="test",
        aws_secret_access_key="test",
        region_name="us-east-1",
        config=Config(s3={"addressing_style": "path"}),
    )

    buckets = s3.list_buckets()["Buckets"]
    print(f"Conectare la MiniStack reușită: {ENDPOINT}")

    if BUCKET not in [bucket["Name"] for bucket in buckets]:
        s3.create_bucket(Bucket=BUCKET)
        print(f"Bucket creat: {BUCKET}")
    else:
        print(f"Bucket existent: {BUCKET}")

    ORIGINAL.write_text(
        "Demonstrație AWS S3 cu MiniStack.\n"
        "Acest document este încărcat și descărcat prin Boto3.\n",
        encoding="utf-8",
    )

    s3.upload_file(str(ORIGINAL), BUCKET, OBJECT_KEY)
    print(f"Fișier încărcat: {OBJECT_KEY}")

    print("Obiecte disponibile în bucket:")
    paginator = s3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=BUCKET):
        for item in page.get("Contents", []):
            print(f"  - {item['Key']} ({item['Size']} bytes)")

    s3.download_file(BUCKET, OBJECT_KEY, str(DOWNLOADED))
    print(f"Fișier descărcat: {DOWNLOADED.name}")

    if ORIGINAL.read_bytes() != DOWNLOADED.read_bytes():
        raise RuntimeError("Fișierul descărcat diferă de original.")

    print("VERIFICARE REUȘITĂ: fișierele sunt identice.")


if __name__ == "__main__":
    try:
        main()
    except (BotoCoreError, ClientError, OSError, RuntimeError) as error:
        print(f"EROARE: {error}")
        raise SystemExit(1)