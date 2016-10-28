
import os
import yaml


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', '..', 'var', 'log'))

secrets = yaml.load(open(os.path.join(BASE_DIR, '..', 'secrets.yml')).read())

SECRET_KEY = secrets['DJANGO_SECRET_KEY']

ALLOWED_HOSTS = ['192.168.101.2', '.roysss.com']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # start local apps
    'roysss.apps.common',
    'roysss.apps.error',
    'roysss.apps.home',
    'roysss.apps.shop',
]


MIDDLEWARE = [
    'roysss.apps.common.middleware.RequestIdMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'roysss.apps.common.middleware.UuidMiddleware',
]

ROOT_URLCONF = 'roysss.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'roysss.jinja2.environment.Jinja2Environment',
        },
    },
]

WSGI_APPLICATION = 'roysss.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STRIPE = {
    'SECRET_KEY': None,
    'PUBLISHABLE_KEY': None,
}

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(request_id)s %(module)s %(funcName)s %(lineno)s %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(request_id)s %(message)s'
        },
    },
    'filters': {
        'inject_request_id': {
            '()': 'roysss.apps.common.roysss_logging.filters.RequestIdFilter',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file_debug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'roysss-debug.log'),
            'formatter': 'simple',
            'filters': ['inject_request_id'],
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'roysss-error.log'),
            'formatter': 'verbose',
            'filters': ['inject_request_id'],
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'roysss': {
            'handlers': ['console', 'file_debug', 'file_error'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}


REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 2
