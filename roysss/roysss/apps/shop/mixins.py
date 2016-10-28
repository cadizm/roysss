
from django.conf import settings
from django.http import Http404

from roysss.apps.shop.models import Style


class StripeMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(StripeMixin, self).get_context_data(*args, **kwargs)

        stripe_keys = settings.STRIPE.copy()
        stripe_keys.pop('SECRET_KEY')

        context.update(stripe=stripe_keys)

        return context


class StyleMixin(object):
    def dispatch(self, *args, **kwargs):
        try:
            style_id = kwargs.get('style_id', None)
            self.style = Style.objects.get(style_id=style_id)

        except Style.DoesNotExist:
            raise Http404

        return super(StyleMixin, self).dispatch(*args, **kwargs)
