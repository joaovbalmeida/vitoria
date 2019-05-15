from django.urls import path
from . import views

urlpatterns = [
    path('', views.ConstructionView.as_view(), name='construction'),
]