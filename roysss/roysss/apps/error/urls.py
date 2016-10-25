
from django.conf.urls import url

from roysss.apps.error.views import (Error400View, Error403View, Error404View,
    Error500View,
    )


urlpatterns = [
    url(r'^400/$', Error400View.as_view(), name='error_400'),
    url(r'^403/$', Error403View.as_view(), name='error_403'),
    url(r'^404/$', Error404View.as_view(), name='error_404'),
    url(r'^500/$', Error500View.as_view(), name='error_500'),
]
