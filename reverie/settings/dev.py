# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

import os

from reverie.settings.base import *


## Configuration

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), # noqa
    }
}

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SECRET_KEY = '11@o_6o8u9d%%4c29hi7v@3ty(g^-7s63^dtipj*qu1sl#mvk$' # noqa

## Third-Party Module Configuration

# django-registration-redux
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_OPEN = False
