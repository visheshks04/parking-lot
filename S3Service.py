import boto3


class S3Service:
    def __init__(self, bucket_name, aws_access_key, aws_secret_key):
        self.bucket_name = bucket_name
        self.aws_access_key = aws_access_key
        self.aws_secret_key = aws_secret_key

    def save(self, file_name):
        s3 = boto3.client('s3', aws_access_key_id=self.aws_access_key, aws_secret_access_key=self.aws_secret_key)
        try:
            s3.upload_file('parking_lot.json', self.bucket_name, file_name)
            print(f"File '{file_name}' uploaded successfully to '{self.bucket_name}' bucket on S3.")
        except Exception as e:
            print(f"Error uploading file to S3: {e}")
