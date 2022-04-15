from django.urls import path
from . import views

app_name = "app_user"

urlpatterns = [
    path('registrarse/', views.UserCreateView.as_view(), name='user-register'),
    path('registrarse/<msj>/', views.UserCreateView.as_view(), name='user-register'),
    path('', views.LoginFormView.as_view(), name='user-login'),
    path('cerrar-sesion/',views.logout_,name='user-logout'),
]