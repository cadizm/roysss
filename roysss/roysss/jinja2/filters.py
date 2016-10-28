
import jinja2

from roysss.apps.common import utils


@jinja2.contextfilter
def currency(context, value, **kwargs):
    return utils.currency(value, **kwargs)
