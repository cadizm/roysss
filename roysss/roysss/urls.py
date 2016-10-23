
from django.conf.urls import (url, include, handler400, handler403,
    handler404, handler500,
    )

import roysss.apps.home.urls
import roysss.apps.shop.urls

from roysss.apps.common.views import (Handler400View, Handler403View,
    Handler404View, Handler500View,
    )


urlpatterns = [
    url(r'^', include(roysss.apps.home.urls)),
    url(r'^shop/', include(roysss.apps.shop.urls)),
]


handler400 = Handler400View.as_view()
handler403 = Handler403View.as_view()
handler404 = Handler404View.as_view()
handler500 = Handler500View.as_view()
