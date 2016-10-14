
from datetime import datetime

from django.views.generic.base import TemplateView

from .mixins import StripeMixin


class ShopView(StripeMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShopView, self).get_context_data(*args, **kwargs)

        context.update(
            year=datetime.now().year,
        )

        return context
