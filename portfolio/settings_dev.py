from portfolio.settings_common import *

DEBUG = True
SECRET_KEY = '^dte)152$+w47_)ck5ie=4^0a9u#r0t)g45dj8^*8y2q#483jf'

ALLOWED_HOSTS = ['127.0.0.1', 'testserver', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('MONGO_ENGINE', 'django.db.backends.sqlite3'),
        'HOST': os.environ.get('MONGO_HOST', 'localhost'),
        'USER': os.environ.get('MONGO_USER', 'user'),
        'PASSWORD': os.environ.get('MONGO_PASSWORD', 'password'),
        'NAME': os.environ.get('MONGO_DEV_DATABASE', os.path.join(BASE_DIR, 'db.sqlite3')),
    }
}
