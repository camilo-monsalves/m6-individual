from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='inicio'),
    path('clientes/', views.cliente, name='cliente'),
    path('registro/', views.registro, name='registro'),
]
