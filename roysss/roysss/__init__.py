
from werkzeug.local import LocalStack, LocalProxy

_request_ctx_stack = LocalStack()

current_request = LocalProxy(lambda: _request_ctx_stack.top)
