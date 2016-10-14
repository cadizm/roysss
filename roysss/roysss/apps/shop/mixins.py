
from django.conf import settings


class StripeMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(StripeMixin, self).get_context_data(*args, **kwargs)

        context.update(stripe=settings.STRIPE)

        return context
