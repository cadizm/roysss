
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from roysss.apps.common.mixins import GetMethodNotAllowedMixin
from roysss.apps.common.views import BaseView, BaseTemplateView, Handler400View

from roysss.apps.shop.checkout import stripe_checkout
from roysss.apps.shop.exceptions import InsufficientInventoryError
from roysss.apps.shop.mixins import StripeMixin
from roysss.apps.shop.models import Inventory

import logging
logger = logging.getLogger(__name__)


class ShopView(StripeMixin, BaseTemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShopView, self).get_context_data(*args, **kwargs)

        inventory = {}
        for inv in Inventory.objects.all():
            inventory.update(**inv.style_quantity())

        context.update(
            inventory=inventory,
            )

        return context


class CheckoutView(GetMethodNotAllowedMixin, BaseView):

    def post(self, *args, **kwargs):
        try:
            kwargs = {k: v for k,v in self.request.POST.items()}
            charge = stripe_checkout(self.request, **kwargs)

            return HttpResponse(charge.order.number)

        except InsufficientInventoryError:
            logger.error('Insufficient inventory')
            response = HttpResponseRedirect(reverse('shop'))
            return response

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
