
import json

from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect

from roysss.apps.common.mixins import GetMethodNotAllowedMixin, RedisMixin
from roysss.apps.common.utils import context_json_encode
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


class CheckoutView(RedisMixin, GetMethodNotAllowedMixin, BaseView):

    EX_SECS = 1800  # confirmation expiration seconds (30 min)

    def post(self, *args, **kwargs):
        try:
            kwargs = {k: v for k,v in self.request.POST.items()}
            charge = stripe_checkout(self.request, **kwargs)

            return self._confirmation_response(charge)

        except InsufficientInventoryError:
            logger.error('Insufficient inventory')
            return HttpResponseRedirect(reverse('shop'))

        except Exception as e:
            logger.exception(e)
            return HttpResponseRedirect(reverse('checkout_error'))

    def _confirmation_response(self, charge):
        key = '%s:%s' % (self.request.session['uuid'], charge.order.number)
        val = json.dumps(context_json_encode(charge.order.__dict__))
        self.redis.set(key, val, ex=self.EX_SECS)

        kwargs = dict(number=charge.order.number)
        response = HttpResponseRedirect(reverse('confirmation', kwargs=kwargs))

        return response


class CheckoutErrorView(Handler400View):
    template_name = 'checkout_error.html'


class ConfirmationView(RedisMixin, BaseTemplateView):
    template_name = 'confirmation.html'

    def dispatch(self, *args, **kwargs):
        key = '%s:%s' % (self.request.session['uuid'], kwargs.get('number', None))
        self.order = json.loads(self.redis.get(key))

        if not self.order:
            raise Http404

        return super(ConfirmationView, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(ConfirmationView, self).get_context_data(*args, **kwargs)

        context.update(
            order=self.order,
            )

        return context
