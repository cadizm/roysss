
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from roysss.apps.common.mixins import GetMethodNotAllowedMixin
from roysss.apps.common.views import BaseView, BaseTemplateView, Handler400View

from roysss.apps.shop.checkout import stripe_checkout
from roysss.apps.shop.mixins import StripeMixin

import logging
logger = logging.getLogger(__name__)


class ShopView(StripeMixin, BaseTemplateView):
    template_name = 'index.html'


class CheckoutView(GetMethodNotAllowedMixin, BaseView):

    def post(self, *args, **kwargs):
        try:
            # TODO: inventory check
            kwargs = {k: v for k,v in self.request.POST.items()}
            charge = stripe_checkout(self.request, **kwargs)

            return HttpResponse(charge.order.number)

        except Exception as e:
            logger.exception(e)
            return HttpResponseRedirect(reverse('checkout_error'))


class CheckoutErrorView(Handler400View):
    template_name = 'checkout_error.html'


class ConfirmationView(BaseTemplateView):
    template_name = 'confirmation.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ConfirmationView, self).get_context_data(*args, **kwargs)

        return context
