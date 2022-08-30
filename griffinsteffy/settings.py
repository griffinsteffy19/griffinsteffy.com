"""
Django settings for griffinsteffy project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import sys
import dj_database_url
from django.core.management.utils import get_random_secret_key
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
# Debug Mode
DEBUG = os.getenv("DEBUG", "False") ==  "True"

#Access Remote Server
REMOTE_SERVER = os.getenv("REMOTE_SERVER", "False") == "True"

#Location
LOCAL_DEVELOPMENT = os.getenv("LOCAL_DEVELOPMENT", "False") == "True"

if LOCAL_DEVELOPMENT:
    from . import local
    LOCAL_AWS_ACCESS_KEY_ID = local.AWS_ACCESS_KEY_ID
    LOCAL_AWS_SECRET_ACCESS_KEY = local.AWS_SECRET_ACCESS_KEY
    LOCAL_AWS_STORAGE_BUCKET_NAME = local.AWS_STORAGE_BUCKET_NAME
    LOCAL_AWS_S3_ENDPOINT_URL = local.AWS_S3_ENDPOINT_URL
    LOCAL_AWS_S3_CUSTOM_DOMAIN = local.AWS_S3_CUSTOM_DOMAIN
    LOCAL_SECRET_KEY = local.DJANGO_SECRET_KEY
    LOCAL_PLAID_CLIENT_ID = local.PLAID_CLIENT_ID
    LOCAL_PLAID_SECRET = local.PLAID_SANDBOX_KEY
else:
    LOCAL_AWS_ACCESS_KEY_ID = ""
    LOCAL_AWS_SECRET_ACCESS_KEY = ""
    LOCAL_AWS_STORAGE_BUCKET_NAME = ""
    LOCAL_AWS_S3_ENDPOINT_URL = ""
    LOCAL_AWS_S3_CUSTOM_DOMAIN = ""
    LOCAL_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = LOCAL_SECRET_KEY

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'base',
    'category',
    'about',
    'taggit',
    'crispy_forms',
    'storages',
    'mathfilters',
    'hitcount',
    'django_cleanup.apps.CleanupConfig', # place last
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'griffinsteffy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'media'),
            # os.path.join(MEDIA_URL, '')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'griffinsteffy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if LOCAL_DEVELOPMENT is True:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    if os.getenv("DATABASE_URL", None) is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Django Hitcount

HITCOUNT_HITS_PER_IP_LIMIT = 1
HITCOUNT_KEEP_HIT_IN_DATABASE = { 'days': 30 }

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

if REMOTE_SERVER:
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", LOCAL_AWS_ACCESS_KEY_ID)
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", LOCAL_AWS_SECRET_ACCESS_KEY)

    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME", LOCAL_AWS_STORAGE_BUCKET_NAME)
    AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL", LOCAL_AWS_S3_ENDPOINT_URL)
    # I enabled the CDN, so you get a custom domain. Use the end point in the AWS_S3_CUSTOM_DOMAIN setting. 
    AWS_S3_CUSTOM_DOMAIN = os.getenv("AWS_S3_CUSTOM_DOMAIN", LOCAL_AWS_S3_CUSTOM_DOMAIN)
    AWS_S3_ADDRESSING_STYLE = "virtual" 
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    AWS_DEFAULT_ACL = 'public-read'

    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'  

    # Use AWS_S3_ENDPOINT_URL here if you haven't enabled the CDN and got a custom domain. 
    STATIC_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, 'static')
    STATIC_ROOT = 'static/'

    MEDIA_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, 'media')
    MEDIA_ROOT = 'media/'
else:

    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    STATIC_URL = "/static/"
    # STATICFILES_DIRS = (os.path.join(BASE_DIR, "static/"),)

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
