from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class ConstructionView(TemplateView):
    template_name = "construction.html"

    def get_context_data(self, **kwargs):
        context = super(ConstructionView, self).get_context_data(**kwargs)
        return context

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        return context
        
class ProductionView(TemplateView):
    template_name = "production.html"

    def get_context_data(self, **kwargs):
        context = super(ProductionView, self).get_context_data(**kwargs)
        return context

class FleetView(TemplateView):
    template_name = "fleet.html"

    def get_context_data(self, **kwargs):
        context = super(FleetView, self).get_context_data(**kwargs)
        return context

class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        return context