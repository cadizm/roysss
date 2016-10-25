
from django.core.exceptions import SuspiciousOperation, PermissionDenied
from django.http import Http404

from roysss.apps.common.views import BaseView


class Error400View(BaseView):
    def dispatch(self, *args, **kwargs):
        raise SuspiciousOperation


class Error403View(BaseView):
    def dispatch(self, *args, **kwargs):
        raise PermissionDenied


class Error404View(BaseView):
    def dispatch(self, *args, **kwargs):
        raise Http404


class Error500View(BaseView):
    def dispatch(self, *args, **kwargs):
        assert True == False
