
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

import socket

from common import *


STRIPE['SECRET_KEY'] = secrets['STRIPE_LIVE_SECRET_KEY']
STRIPE['PUBLISHABLE_KEY'] = secrets['STRIPE_LIVE_PUBLISHABLE_KEY']

if 'vagrant' in socket.gethostname():
    STRIPE['SECRET_KEY'] = secrets['STRIPE_TEST_SECRET_KEY']
    STRIPE['PUBLISHABLE_KEY'] = secrets['STRIPE_TEST_PUBLISHABLE_KEY']
