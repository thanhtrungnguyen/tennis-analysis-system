# config/settings/s3.py
AWS_ACCESS_KEY_ID = 'your-access-key-id'
AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'
AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
AWS_S3_REGION_NAME = 'your-region'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_DEFAULT_ACL = None

# File storage configurations
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Static file configuration (optional)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# URL settings for media
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
