from django.urls import path
from . import views

urlpatterns = [
    path('registro_usuario', views.registro_user, name='registro-usuario'),
    path('login_usuario', views.login_user, name='login-usuario'),
    path('logout_usuario', views.logout_user, name='logout-usuario')
]