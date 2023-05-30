import os

from settings.env import BASE_DIR, env_to_enum

from enum import Enum


class FileUploadStrategy(Enum):
    STANDARD = "standard"
    DIRECT = "direct"


class FileUploadStorage(Enum):
    LOCAL = "local"
    S3 = "s3"



FILE_UPLOAD_STRATEGY = env_to_enum(
    FileUploadStrategy,
    os.environ.get("FILE_UPLOAD_STRATEGY", default="standard")
)
FILE_UPLOAD_STORAGE = env_to_enum(
    FileUploadStorage,
    os.environ.get("FILE_UPLOAD_STORAGE", default="local")
)

FILE_MAX_SIZE = int(os.environ.get("FILE_MAX_SIZE", default=10485760))  # 10 MiB

if FILE_UPLOAD_STORAGE == FileUploadStorage.LOCAL:
    MEDIA_ROOT_NAME = "media"
    MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_ROOT_NAME)
    MEDIA_URL = f"/{MEDIA_ROOT_NAME}/"

if FILE_UPLOAD_STORAGE == FileUploadStorage.S3:
    # Using django-storages
    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    AWS_S3_ACCESS_KEY_ID = os.environ.get("AWS_S3_ACCESS_KEY_ID")
    AWS_S3_SECRET_ACCESS_KEY = os.environ.get("AWS_S3_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME")
    AWS_S3_SIGNATURE_VERSION = os.environ.get("AWS_S3_SIGNATURE_VERSION", default="s3v4")

    # https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl
    AWS_DEFAULT_ACL = os.environ.get("AWS_DEFAULT_ACL", default="private")

    AWS_PRESIGNED_EXPIRY = int(os.environ.get("AWS_PRESIGNED_EXPIRY", default=10))  # seconds

    _AWS_S3_CUSTOM_DOMAIN = os.environ.get("AWS_S3_CUSTOM_DOMAIN", default="")

    if _AWS_S3_CUSTOM_DOMAIN:
        AWS_S3_CUSTOM_DOMAIN = _AWS_S3_CUSTOM_DOMAIN
