from reverie.settings.base import *

DEBUG = True
SECRET_KEY = '11@o_6o8u9d%%4c29hi7v@3ty(g^-7s63^dtipj*qu1sl#mvk$' # noqa

# django-registration-redux
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = '/'

# email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
