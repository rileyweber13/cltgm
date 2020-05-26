"""
Django settings for cltgm project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import netifaces

# Find out what the IP addresses are at run time
# This is necessary because otherwise Gunicorn will reject the connections
def ip_addresses():
    ip_list = []
    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        for x in (netifaces.AF_INET, netifaces.AF_INET6):
            if x in addrs:
                ip_list.append(addrs[x][0]['addr'])
    return ip_list

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# include config file for server/dev settings, secrets
import configparser
config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'cltgm/config.ini'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['secrets']['django_secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config['server_settings'].getboolean('debug')

# Discover our IP address
ALLOWED_HOSTS = ip_addresses()

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'cltgm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'cltgm/templates'
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

WSGI_APPLICATION = 'cltgm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config['db_info']['db_name'],
        'USER': config['db_info']['user_name'],
        'PASSWORD': config['secrets']['db_password'],
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    'cltgm/static'
]

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

# Allow Django from all hosts. This snippet is installed from
# /var/lib/digitalocean/allow_hosts.py

import os
import netifaces

# Find out what the IP addresses are at run time
# This is necessary because otherwise Gunicorn will reject the connections
def ip_addresses():
    ip_list = []
    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        for x in (netifaces.AF_INET, netifaces.AF_INET6):
            if x in addrs:
                ip_list.append(addrs[x][0]['addr'])
    return ip_list

# Discover our IP address
ALLOWED_HOSTS = ip_addresses()
if config['server_settings']['additional_allowed_ips'] != '':
    ALLOWED_HOSTS += config['server_settings']['additional_allowed_ips'].split(',')

if config['server_settings'].getboolean('email_debug'):
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = '465'
    EMAIL_USE_SSL = True
    # EMAIL_PORT = '587'
    # EMAIL_USE_TLS = True
    EMAIL_HOST_USER = config['server_settings']['smtp_login_username']
    EMAIL_HOST_PASSWORD = config['secrets']['email_smtp_password']
