"""
Django settings for havytours project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import dj_database_url  # For Heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7jf)^t-_)6zz=3pu&h0zv^yx1@@zot1t1pds@+%-^n_)gncb5v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# TODO change to False for production

# For Heroku
ALLOWED_HOSTS = ['havytours.herokuapp.com', '.havytours.com', '127.0.0.1']

# Application definition
# 'whitenoise.runserver_nostatic' - must be before 'django.contrib.staticfiles' to run Whitenoise in development
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
]

# Add whitenoise
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'havytours.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'havytours.wsgi.application'


################################################################
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
################################################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


################################################################
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
################################################################
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


################################################################
# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
################################################################
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


################################################################
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
################################################################
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# for /static/root/favicon.ico
WHITENOISE_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'root')

TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)

# for compression. May cause Error 500
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


################################################################
# For Email
################################################################
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'web-administrator'
EMAIL_HOST_PASSWORD = 'H4ck Me! d'
EMAIL_PORT = 587
EMAIL_USE_TLS = True



################################################################
# Configure Django App for Heroku.
################################################################
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 600