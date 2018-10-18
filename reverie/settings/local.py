import logging.config
import os

from reverie.settings.base import * # noqa

DEBUG = True
SECRET_KEY = '11@o_6o8u9d%%4c29hi7v@3ty(g^-7s63^dtipj*qu1sl#mvk$' # noqa

# django-registration-redux
ACCOUNT_ACTIVATION_DAYS = 7

# email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# django-two-factor-auth
TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.fake.Fake'

# Databases
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), # noqa
  }
}


# Development Logging Configuration
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        'two_factor': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
})
