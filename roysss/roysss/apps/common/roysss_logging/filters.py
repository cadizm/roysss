
import logging

from roysss import current_request


class RequestIdFilter(logging.Filter):

    def filter(self, record):
        record.request_id = current_request.request_id
        return True
