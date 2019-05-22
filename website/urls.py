from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('quemsomos', views.AboutView.as_view(), name='about'),
    path('producao', views.ProductionView.as_view(), name='production'),
    path('nossafrota', views.FleetView.as_view(), name='fleet'),
    path('contato', views.ContactView.as_view(), name='contact'),
]