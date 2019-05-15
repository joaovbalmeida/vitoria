from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class ConstructionView(TemplateView):
    template_name = "construction.html"

    def get_context_data(self, **kwargs):
        context = super(ConstructionView, self).get_context_data(**kwargs)
        return context
