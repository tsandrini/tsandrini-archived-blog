from tsandrini.settings.base import *

DEBUG = False

SECRET_KEY = ''

ALLOWED_HOSTS = [
]

INTERNAL_IPS = [
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

HTML_MINIFY = True
