#encoding:utf-8
"""
Django settings for emergencycare project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR    = os.path.dirname(os.path.dirname(__file__))
SITE_ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*wwias0#u)7s4s2+*uf5bvq^_(lgr9=9sjjid0qbr*2#+=78p#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']
SITE_ID = 1
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ficha',
    'diagnostico',
    'sesion',
    'bootstrapform',
    'bootstrap3_datetime',
    )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#    'administration.login_required_middleware.RequireLoginMiddleware',

)

ROOT_URLCONF = 'emergencycare.urls'

WSGI_APPLICATION = 'emergencycare.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'

USE_I18N    = True
USE_L10N    = True
USE_TZ      = True


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
# 'django.template.loaders.eggs.Loader',
)

  

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
 )

import django.conf.global_settings as DEFAULT_SETTINGS

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'django.core.context_processors.static'
)

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT,'static_root'),
)

STATIC_ROOT = 'media'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT,'templates'),
)

MEDIA_ROOT = os.path.join(SITE_ROOT,'media/')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL  = '/admin/'
LOGIN_URL           = '/login/'
LOGIN_REQUIRED_URLS = ( r'/admin(|/)(.*)$',)

LOGIN_REQUIRED_URLS_EXCEPTIONS = (
    r'/(login|logout)(|/)$',
)

PATH = '/var/www/emergencycare/'
