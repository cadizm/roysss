
from django.conf.urls import url

from roysss.apps.shop.views import ShopView


urlpatterns = [
    url(r'^$', ShopView.as_view(), name='shop'),
]
