"""
Django settings for means project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import configparser
import base64

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config_file = os.path.join(BASE_DIR, "config" + os.sep + "config.ini")
config = configparser.ConfigParser()
config.read(config_file)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xz3t#m#8&vj^7zwhcr&b+cw*_l0lw=*^)e0*z82y^pzh-nep@g'

# SECURITY WARNING: don't run with debug turned on in production!


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
online = True
if online:
    DEBUG = False
    ALLOWED_HOSTS = ['www.meanslab.com', 'meanslab.com']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': "means",
            'USER': 'root',
            'PASSWORD': 'zjss123456',
            'HOST': 'hwsrv-838845.hostwindsdns.com',
        }
    }
else:
    DEBUG = True
    ALLOWED_HOSTS = []
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'collection',
    'search',
    'predict',
    'user',
    'team',
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

ROOT_URLCONF = 'means.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'collection', 'templates'),
            os.path.join(BASE_DIR, 'search', 'templates'),
            os.path.join(BASE_DIR, 'predict', 'templates'),
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

WSGI_APPLICATION = 'means.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static', 'means'),
    os.path.join(BASE_DIR, 'collection', 'static', 'collection'),
    os.path.join(BASE_DIR, 'search', 'static', 'search'),
    os.path.join(BASE_DIR, 'predict', 'static', 'predict'),
]

AUTH_USER_MODEL = 'user.user'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"  # Default

pwd = config.get('user', 'pwd')
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_HOST_USER = 'means_service@hotmail.com'
EMAIL_HOST_PASSWORD = base64.b64decode(base64.b64decode(pwd)).decode()
EMAIL_PORT = 587
EMAIL_SECURITY = 'STARTTLS'
