
from datetime import datetime

from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponse

from roysss.apps.common.views import BaseView, BaseTemplateView

from roysss.apps.shop.checkout import stripe_checkout
from roysss.apps.shop.mixins import StripeMixin

import logging
logger = logging.getLogger(__name__)


class ShopView(StripeMixin, BaseTemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShopView, self).get_context_data(*args, **kwargs)

        context.update(
            current_year=datetime.now().year,
        )

        return context


class CheckoutView(BaseView):

    def dispatch(self, *args, **kwargs):
        if self.request.method == 'GET':
            return HttpResponseNotAllowed('Method not allowed')

        return super(CheckoutView, self).dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        try:
            # TODO: inventory check
            # TODO: stripe email confirmation

            kwargs = {k: v for k,v in self.request.POST.items()}
            charge = stripe_checkout(self.request, **kwargs)

            return HttpResponse(charge.order.number)

        except Exception as e:
            logger.exception(e)
            return HttpResponseBadRequest(self.request.request_id)


class ConfirmationView(BaseTemplateView):
    template_name = 'confirmation.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShopView, self).get_context_data(*args, **kwargs)

        context.update(
            year=datetime.now().year,
        )

        return context
