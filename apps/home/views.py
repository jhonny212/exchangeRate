import re
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#local
from .models import ExchangeRate
from . import functions
from . import forms

#List table of exchange rate
class ExchangeRateListView(LoginRequiredMixin,ListView):
    model = ExchangeRate
    template_name = "Home/listExchange.html"
    context_object_name = 'exchanges'

    #filter queryset
    def get_queryset(self):
        queryset = super(ExchangeRateListView, self).get_queryset()
        if 'filter' in self.request.GET:
            queryset = ExchangeRate.objects.filter(
                date__lte=self.request.GET['filter']
            )
        else:
            queryset = ExchangeRate.objects.all()
        return queryset

#Register a new exchange rate
class ExchangeCreateView(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):
        return render(request,"Home/addExchange.html")

    def post(self, request, *args):
        msj = ""
        status = 200
        try:
            if 'init' in request.POST:
                date = request.POST['init']
                res = functions.get_exchange_rate(date)
                if not ExchangeRate.objects.filter(date=date).exists():
                    ExchangeRate.objects.create(
                        date=date,
                        sale_price=res['venta'],
                        purchase_price=res['compra']
                    )
                    msj = "Registro guardado"
                else:
                    msj = "Ya existe un registro en esta fecha"
            else:
                msj = "Debe ingresar una fecha"
                status = 400
        except Exception as e:
            msj = "Error al registrar intercambio de moneda, intente de nuevo"
            status = 500
        return JsonResponse({
            "msj":msj
        },status=status)

#Update a register
class ExchangeReateUpdateView(LoginRequiredMixin,UpdateView):
    model = ExchangeRate
    template_name = "Home/editExchange.html"
    form_class = forms.ExchangeRateForm
    success_url = '.'

#Delete a register
class ExchangeRateDeleteView(LoginRequiredMixin,DeleteView):
    model = ExchangeRate
    template_name = "Home/deleteExchange.html"
    context_object_name = 'exchange_rate'
    success_url = reverse_lazy('app_home:home-get-all')

#get api of exchange rate
@login_required
def get_exchange_rate(request):
    try:
        response =functions.get_exchange_rate(request.GET['date'])
        return JsonResponse(response,status=200)
    except:
        return JsonResponse({},status=400)