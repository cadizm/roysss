
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

from common import *


STRIPE['SECRET_KEY'] = secrets['STRIPE_LIVE_SECRET_KEY']
STRIPE['PUBLISHABLE_KEY'] = secrets['STRIPE_LIVE_PUBLISHABLE_KEY']
