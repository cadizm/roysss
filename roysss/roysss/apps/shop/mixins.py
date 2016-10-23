
from django.conf import settings


class StripeMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(StripeMixin, self).get_context_data(*args, **kwargs)

        stripe_keys = settings.STRIPE.copy()
        stripe_keys.pop('SECRET_KEY')

        context.update(stripe=stripe_keys)

        return context
