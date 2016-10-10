
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView


class HomeView(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('shop'))
