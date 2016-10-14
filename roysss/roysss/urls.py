
from django.conf.urls import url, include

import roysss.apps.home.urls
import roysss.apps.shop.urls


urlpatterns = [
    url(r'^', include(roysss.apps.home.urls)),
    url(r'^shop', include(roysss.apps.shop.urls)),
]
