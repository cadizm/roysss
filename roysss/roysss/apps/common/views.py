
from datetime import datetime

from django.conf import settings
from django.core.serializers import settings
from django.http import JsonResponse

from django.views.generic.base import View, TemplateView

from roysss.apps.common.utils import context_json_encode


class BaseView(View):
    status_code = 200

    def get_context_data(self, *args, **kwargs):
        context = super(BaseView, self).get_context_data(*args, **kwargs)

        context.update(
            request_id=self.request.request_id,
            current_year=datetime.now().year,
            )

        return context

    def render_to_response(self, context, **kwargs):
        kwargs['status'] = self.status_code

        if 'context' in self.request.GET and settings.DEBUG:
            return JsonResponse(context_json_encode(context), safe=False)

        return super(BaseView, self).render_to_response(context, **kwargs)


class BaseTemplateView(BaseView, TemplateView):
    template_name = None


class Handler400View(TemplateView):
    """
    Handles exception django.core.exceptions.SuspiciousOperation
    """
    status_code = 400
    template_name = '400.html'


class Handler403View(TemplateView):
    """
    Handles exception django.core.exceptions.PermissionDenied
    """
    status_code = 403
    template_name = '403.html'


class Handler404View(BaseTemplateView):
    """
    Handles exception django.http.Http404
    """
    status_code = 404
    template_name = '404.html'


class Handler500View(TemplateView):
    """
    Handles view runtime exceptions
    """
    status_code = 500
    template_name = '500.html'
