from portfolio.settings_common import *
DEBUG = True
SECRET_KEY = os.getenv('DJANGO_PROD_SECRET_KEY')

ALLOWED_HOSTS = ['.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('MONGO_ENGINE', 'django.db.backends.sqlite3'),
        'HOST': os.environ.get('MONGO_HOST', 'localhost'),
        'USER': os.environ.get('MONGO_USER', 'user'),
        'PASSWORD': os.environ.get('MONGO_PASSWORD', 'password'),
        'NAME': os.environ.get('MONGO_PROD_DATABASE', os.path.join(BASE_DIR, 'db.sqlite3')),
    }
}
