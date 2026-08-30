import boto3


class S3Storage:

    def __init__(
        self,
        bucket
    ):
        self.bucket = bucket
        self.client = boto3.client("s3")

    def upload(
        self,
        file_path,
        key
    ):
        self.client.upload_file(
            file_path,
            self.bucket,
            key
        )