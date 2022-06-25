from pkg_resources import DEVELOP_DIST
from griffinsteffy.settings import DEVELOPMENT_MODE
from storages.backends.s3boto3 import S3Boto3Storage
import os
class StaticStorage(S3Boto3Storage):
	bucket_name = os.getenv("AWS_STORAGE_BUCKET_NAME", "griffinsteffystatic")
	location = 'static'

class MediaStorage(S3Boto3Storage):
	bucket_name = os.getenv("AWS_STORAGE_BUCKET_NAME", "griffinsteffystatic")
	location = 'media'