"""
Brief: Django settings for config project.
Generated by 'django-admin startproject' using Django 5.0.6.

Description: This file contains the settings for the Django project.
It includes the database configuration, CORS settings, allowed hosts,
secret key, debug mode, etc.

Author: Divij Sharma <divijs75@gmail.com>
"""
import os
import datetime
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv()


# Get the project secret key from the environment variable
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY = os.environ.get('PROJECT_SECRET_KEY', 'default')

# Get the debug mode from the environment variable
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('ENV', 'production') == 'development'

# Get the allowed hosts from the environment variable
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "djoser",
    "social_django",
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework.authtoken",
    "core",
    "live",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# Get the CORS allowed origins from the environment variable
CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', '').split(',')

# Template settings
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = "config.wsgi.application"

# Databse Configuration
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.mysql"),
        "NAME": os.getenv("DB_NAME", "spapi"),
        "USER": os.getenv("DB_USER", "root"),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", "127.0.0.1"),
        "PORT": os.getenv("DB_PORT", "3306"),
    }
}


# Password validation
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
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "static/"

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Override the default user model

AUTH_USER_MODEL = "core.User"

# Email settings

EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
MAILER_EMAIL_BACKEND = os.environ.get('MAILER_EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Authentication backends

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# REST Framework settings

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Simple JWT settings config

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=1)
}


# OAuth settings

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('GOOGLE_OAUTH2_KEY', '')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('GOOGLE_OAUTH2_SECRET', '')
SOCIAL_AUTH_ALLOWED_REDIRECT_URIS = os.environ.get('SOCIAL_AUTH_ALLOWED_REDIRECT_URIS', '').split(',')
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = [
    'first_name',
    'last_name',
]

# Djoser settings

DJOSER = {
    'SERIALIZERS': {
        'user_create': 'core.serializers.UserCreateSerializer',
        'current_user': 'core.serializers.UserSerializer',
        'user': 'core.serializers.UserSerializer',
    },
    'SEND_ACTIVATION_EMAIL': True,
    'ACTIVATION_URL': 'auth/activate/?uid={uid}&token={token}',
    'PASSWORD_RESET_CONFIRM_URL': 'auth/reset-password/?uid={uid}&token={token}',
    'USERNAME_RESET_CONFIRM_URL': 'auth/reset-username/?uid={uid}&token={token}',
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True
}
DOMAIN = os.environ.get('DOMAIN', 'http://localhost:3000')
SITE_NAME = os.environ.get('SITE_NAME', 'SPAPI')
