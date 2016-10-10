
from django.conf.urls import url, include

import apps.home.urls
import apps.shop.urls


urlpatterns = [
    url(r'^', include(apps.home.urls)),
    url(r'^shop', include(apps.shop.urls)),
]
