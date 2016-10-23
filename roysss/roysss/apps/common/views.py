
from django.conf import settings
from django.http import JsonResponse

from django.views.generic.base import View, TemplateView


class BaseView(View):
    pass


class BaseTemplateView(BaseView, TemplateView):
    status_code = 200

    def get_context_data(self, *args, **kwargs):
        context = super(BaseTemplateView, self).get_context_data(*args, **kwargs)

        context.update(
            request_id=self.request.request_id,
            )

        return context

    def render_to_response(self, *args, **kwargs):
        kwargs['status'] = self.status_code
        return super(BaseTemplateView, self).render_to_response(*args, **kwargs)


class Handler400View(TemplateView):
    """
    Handles exception django.core.exceptions.SuspiciousOperation
    """
    status_code = 400
    template_name = '400.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Handler400View, self).get_context_data(*args, **kwargs)

        return context


class Handler403View(TemplateView):
    """
    Handles exception django.core.exceptions.PermissionDenied
    """
    status_code = 403
    template_name = '403.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Handler403View, self).get_context_data(*args, **kwargs)

        return context


class Handler404View(BaseTemplateView):
    """
    Handles exception django.http.Http404
    """
    status_code = 404
    template_name = '404.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Handler404View, self).get_context_data(*args, **kwargs)

        return context


class Handler500View(TemplateView):
    """
    Handles view runtime exceptions
    """
    status_code = 500
    template_name = '500.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Handler500View, self).get_context_data(*args, **kwargs)

        return context
