
from datetime import datetime, timedelta
from uuid import uuid1

from roysss import _request_ctx_stack

import logging
logger = logging.getLogger(__name__)


class UuidMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        uuid = request.COOKIES.get('uuid', str(uuid1()))

        if 'uuid' not in request.session:
            request.session['uuid'] = uuid

        response = self.get_response(request)

        if 'uuid' not in request.COOKIES:
            expires = datetime.now() + timedelta(days=365*7)
            response.set_cookie('uuid', uuid, expires=expires, httponly=True)

        return response


class RequestIdMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if not hasattr(request, 'request_id'):
            request.request_id = str(uuid1())

        _request_ctx_stack.push(request)

        response = self.get_response(request)

        popped = _request_ctx_stack.pop()

        if popped is not request:
            logger.warning('_request_ctx_stack popped wrong request')

        response['Request-Id'] = request.request_id

        return response
