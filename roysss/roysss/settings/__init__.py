
from common import *

try:
    if DEBUG:
        from dev import *
    else:
        from production import *

except ImportError:
    pass
