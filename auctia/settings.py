"""
Django settings for auctia project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-4ss+#6#(lpepic77$6@=_2@!wsf@^)w1p9)iq^m2uw-t!*h-n5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "market.apps.MarketConfig",
    "accounts.apps.AccountsConfig",
    "items.apps.ItemsConfig",
    "bids.apps.BidsConfig",
    "payment.apps.PaymentConfig",
    "notification.apps.NotificationConfig",


    #installed-packages
    "channels",
    "storages",
    "daguerre",


]





MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_grip.GripMiddleware",
]

ROOT_URLCONF = "auctia.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR/ 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "context_processors.cp.subject_renderer",
            ],
        },
    },
]

#WSGI_APPLICATION = "auctia.wsgi.application"
ASGI_APPLICATION = "auctia.asgi.application"
#channels_setting
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
    },
}



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_URL="/profile/login/"

REDIS_HOST = 'localhost'
REDIS_PORT = 6379


#celery setting
CELERY_BROKER_URL = 'amqp://localhost'


#email_setting
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = 'ac256aefed5912'
EMAIL_HOST_PASSWORD = '088cdb6ba4ffa6'
EMAIL_PORT = '2525'

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID='bad1ee1d-334d-4c11-a686-fdd3ea8fb21d'
AWS_SECRET_ACCESS_KEY='5c8616daf01886479ddcad76169f5d53bba0f28e'
AWS_S3_ENDPOINT_URL='https://s3.ir-thr-at1.arvanstorage.ir'
AWS_STORAGE_BUCKET_NAME='auctia'
AWS_SERVICE_NAME='s3'
AWS_S3_FILE_OVERWRITE=False



