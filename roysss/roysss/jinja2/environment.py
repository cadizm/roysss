
import jinja2

from roysss.jinja2 import filters as roysss_filters


class Jinja2Environment(jinja2.Environment):

    def __init__(self, *args, **kwargs):
        super(Jinja2Environment, self).__init__(*args, **kwargs)

        # http://jinja.pocoo.org/docs/dev/api/#jinja2.Environment.filters
        self.filters.update(
            currency=roysss_filters.currency,
            )

        # http://jinja.pocoo.org/docs/dev/api/#jinja2.Environment.globals
        self.globals.update(
            )
