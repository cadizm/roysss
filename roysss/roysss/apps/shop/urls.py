
from django.conf.urls import url

from roysss.apps.shop.views import (ShopView, ShopStyleView, CheckoutView,
    CheckoutErrorView, ConfirmationView,
    )


urlpatterns = [
    url(r'^$', ShopView.as_view(), name='shop'),
    url(r'^style/(?P<style_id>(\w+))/$', ShopStyleView.as_view(), name='style'),
    url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),
    url(r'^checkout/error/$', CheckoutErrorView.as_view(), name='checkout_error'),
    url(r'^confirmation/(?P<number>[0-9A-Z]{8})/$', ConfirmationView.as_view(), name='confirmation'),
]
