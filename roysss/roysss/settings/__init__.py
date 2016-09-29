
import socket
HOSTNAME = socket.gethostname()

PRODUCTION = False if HOSTNAME == 'l00k' else True
DEBUG = True if not PRODUCTION else False

try:
    if DEBUG:
        from dev import *
    else:
        from production import *

except ImportError:
    pass
