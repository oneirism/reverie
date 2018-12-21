import logging.config

from reverie.settings.base import * # noqa

DEBUG = True
SECRET_KEY = '11@o_6o8u9d%%4c29hi7v@3ty(g^-7s63^dtipj*qu1sl#mvk$' # noqa

# django-registration-redux
ACCOUNT_ACTIVATION_DAYS = 7

# email
EMAIL_BACKEND = 'django_ses.SESBackend'

AWS_SES_REGION_NAME = 'eu-west-1'
AWS_SES_REGION_ENDPOINT = 'email.eu-west-1.amazonaws.com'

DEFAULT_FROM_EMAIL = "Reverie <staging-noreply@oneirism.co>"

# django-two-factor-auth
TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.fake.Fake'

# Databases
DATABASES = {
  'default': {
    'ENGINE': 'zappa_django_utils.db.backends.s3sqlite',
    'NAME': 'dev_sqlite.db',
    'BUCKET': 'db.reverie.devenney.io'
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

AWS_STORAGE_BUCKET_NAME = 'cdn.reverie.devenney.io'
AWS_S3_CUSTOM_DOMAIN = 'cdn.reverie.devenney.io'
AWS_LOCATION = 'dev/static'
STATIC_URL = 'https://{0}/{1}/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
THUMBNAIL_DEFAULT_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

MARKDOWNX_URLS_PATH = '/staging/markdownx/markdownify/'
