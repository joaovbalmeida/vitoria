from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Content, PartnersLogos
from .forms import ContactForm

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
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['partners'] = PartnersLogos.objects.all()
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context
        
class ProductionView(TemplateView):
    template_name = "production.html"

    def get_context_data(self, **kwargs):
        context = super(ProductionView, self).get_context_data(**kwargs)
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context

class FleetView(TemplateView):
    template_name = "fleet.html"

    def get_context_data(self, **kwargs):
        context = super(FleetView, self).get_context_data(**kwargs)
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context

class ContactView(View):

    def get(self, request):
        context = {}
        context['form'] = ContactForm()
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return TemplateResponse(request, 'contact.html', context)

    def post(self, request):
        context = {}
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        try:
            form = ContactForm(request.POST)
            if form.is_valid():
                messages.add_message(request, messages.INFO, 'Obrigado pelo contato!')
                send_mail(
                    'Contato Site Banana Vitória',
                    'Nome: %s, \nEmail: %s, \nMensagem: %s' % (
                        form.cleaned_data['name'],
                        form.cleaned_data['email'],
                        form.cleaned_data['message'],
                    ),
                    'juniorfurlanrj@gmail.com',
                    ['joaovbalmeida@gmail.com'],
                )
                return HttpResponseRedirect(reverse('contact'))
        except Exception as e:
            print(e)
            messages.add_message(request, messages.INFO, 'Não conseguimos enviar a mensagem, por favor tente novamente.')
        context['form'] = form
        return TemplateResponse(request, 'contact.html', context)