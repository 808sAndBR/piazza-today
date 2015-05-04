import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'piazzatodaydb',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = True