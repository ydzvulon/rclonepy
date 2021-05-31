def test__s3path__api():
    import s3path
    import boto3
    from s3path import PureS3Path, register_configuration_parameter, S3Path
    from botocore.client import Config
    minio_resource = boto3.resource(
        's3',
        endpoint_url='http://localhost:27007',
        aws_access_key_id='admin',
        aws_secret_access_key='password',
        config=Config(signature_version='s3v4'),
        region_name='us-east-1')
    
    default_aws_s3_path = PureS3Path('/')
    
    register_configuration_parameter(default_aws_s3_path, resource=minio_resource)

    print(list(S3Path('/test-b').iterdir()))
    print(list(S3Path.from_uri('s3://test-b').iterdir()))