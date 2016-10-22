
from django.conf import settings
from django.http import JsonResponse

from django.views.generic.base import View, TemplateView


class BaseView(View):
    pass


class BaseTemplateView(BaseView, TemplateView):
    pass
