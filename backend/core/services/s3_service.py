import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import logging
import uuid
from django.conf import settings

logger = logging.getLogger(__name__)


def upload_file_to_s3(file, folder='uploads/'):
    """
    Uploads a file to S3 and returns the file URL.

    Args:
        file (File): The file object to upload.
        folder (str): The folder in the S3 bucket where the file will be stored.

    Returns:
        str: The URL of the uploaded file, or None if the upload fails.
    """
    s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME
    )

    # Generate a unique filename
    filename = f"{folder}{uuid.uuid4()}_{file.name}"

    try:
        s3.upload_fileobj(file, settings.AWS_STORAGE_BUCKET_NAME, filename)
        file_url = f"{settings.AWS_S3_CUSTOM_DOMAIN}/{filename}"
        return file_url
    except (NoCredentialsError, ClientError) as e:
        logger.error(f"Failed to upload file to S3: {e}")
        return None
