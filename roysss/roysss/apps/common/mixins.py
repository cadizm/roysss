
from redis import StrictRedis

from django.conf import settings
from django.core.exceptions import SuspiciousOperation


class GetMethodNotAllowedMixin(object):

    def dispatch(self, *args, **kwargs):
        if self.request.method == 'GET':
            raise SuspiciousOperation('Method Not Allowed')

        return super(GetMethodNotAllowedMixin, self).dispatch(*args, **kwargs)


class RedisMixin(object):

    def __init__(self, *args, **kwargs):
        super(RedisMixin, self).__init__(*args, **kwargs)

        host = kwargs.get('host', settings.REDIS_HOST)
        port = kwargs.get('port', settings.REDIS_PORT)
        db = kwargs.get('db', settings.REDIS_DB)

        self.redis = StrictRedis(host=host, port=port, db=db)
