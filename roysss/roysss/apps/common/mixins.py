
from django.core.exceptions import SuspiciousOperation


class GetMethodNotAllowedMixin(object):

    def dispatch(self, *args, **kwargs):
        if self.request.method == 'GET':
            raise SuspiciousOperation('Method Not Allowed')

        return super(GetMethodNotAllowedMixin, self).dispatch(*args, **kwargs)
