
from common import *


INSTALLED_APPS += [
    'django_extensions',
]

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STRIPE['SECRET_KEY'] = secrets['STRIPE_TEST_SECRET_KEY']
STRIPE['PUBLISHABLE_KEY'] = secrets['STRIPE_TEST_PUBLISHABLE_KEY']
