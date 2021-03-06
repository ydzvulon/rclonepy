from pathlib import Path
from minio import Minio
from minio.error import S3Error


def test__minio_basic():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    # [lms3]
    # type = s3
    # env_auth = false
    # access_key_id = admin
    # secret_access_key = password
    # region = us-east-1
    # endpoint = http://127.0.0.1:27007
    import os
    DECK_lms3_ENDPOINT = os.environ.get('DECK_lms3_ENDPOINT', 'http://localhost:27007')
    if DECK_lms3_ENDPOINT.startswith('https'):
        secure = True
        ep = DECK_lms3_ENDPOINT.split('://')[1]
    elif DECK_lms3_ENDPOINT.startswith('http'):
        secure = False
        ep = DECK_lms3_ENDPOINT.split('://')[1]
    else:
        secure = False
        ep = "127.0.0.1:27007"
    client = Minio(
        ep,
        access_key="admin",
        secret_key="password",
        secure=secure
    )

    # Make 'asiatrip' bucket if not exist.
    found = client.bucket_exists("asiatrip")
    if not found:
        client.make_bucket("asiatrip")
    else:
        print("Bucket 'asiatrip' already exists")

    # Upload '/home/user/Photos/asiaphotos.zip' as object name
    # 'asiaphotos-2015.zip' to bucket 'asiatrip'.
    pf = Path(__file__)
    src_p = str(pf.absolute())
    dst_p = pf.name
    
    client.fput_object(
        "asiatrip", dst_p, src_p,
    )
    print(
        f" {src_p} is successfully uploaded as "
        f"object {dst_p} to bucket 'asiatrip'."
    )
