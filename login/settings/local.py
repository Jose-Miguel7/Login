from .base import *




DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
    	'ENGINE': 'django.db.backends.postgresql_psycopg2',
    	'NAME': get_secret('DB_NAME'),
    	'USER': get_secret('USER'),
    	'PASSWORD': get_secret('PASSWORD'),
 		'HOST': 'localhost',
 		'PORT': '8080',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = get_secret('EMAIL')
EMAIL_HOST_PASSWORD = get_secret('EMAIL_KEY')
EMAIL_PORT = 587