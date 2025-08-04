"""
Custom Storage Configuration for AWS S3
Defines custom storage classes for handling static and media files
using AWS S3.
"""
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    Custom storage class for static files (CSS, JS, images).
    Handles storage of static files like CSS, JavaScript, and other assets
    that are part of the application codebase. Uses a specific location
    within the S3 bucket to organize static files separately from media files.
    """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """
    Custom storage class for user-uploaded media files.
    Handles storage of user-uploaded content such as product images and
    profile pictures. Prevents file overwrites to ensure user content is
    preserved and uses a separate location from static files.
    """
    location = settings.MEDIAFILES_LOCATION
    file_overwrite = False
