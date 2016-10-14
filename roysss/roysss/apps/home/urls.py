
from django.conf.urls import url

from roysss.apps.home.views import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
]
