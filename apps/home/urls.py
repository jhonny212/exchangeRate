from django.urls import path
from . import views

app_name = 'app_home'

urlpatterns = [
    path('', views.ExchangeCreateView.as_view(), name='home-add'),
    path('intercambio/', views.get_exchange_rate, name='home-get-exchange'),
    path('intercambios/',views.ExchangeRateListView.as_view(), name='home-get-all'),
    path('editar/<pk>/',views.ExchangeReateUpdateView.as_view(), name='home-edit'),
    path('eliminar/<pk>/',views.ExchangeRateDeleteView.as_view(), name='home-delete'),
]