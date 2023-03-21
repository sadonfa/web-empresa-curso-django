from django.urls import path
from . import views
from webempresa import settings

urlpatterns = [
    path('', views.services, name="services"),  
]


