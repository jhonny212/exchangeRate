from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
#local
from apps.users.models import User
from . import forms

class UserCreateView(FormView):
    model = User
    template_name = "Users/register.html"
    success_url = '.'
    form_class = forms.UserRegisterForm

    def form_valid(self, form) :
        User.objects.create_user(
        form.cleaned_data['username'],
        form.cleaned_data['password'],
        )
        self.success_url = reverse_lazy("app_user:user-register",kwargs={
        'msj':'usuario registrado'
        })
        return super(UserCreateView,self ).form_valid(form)

class LoginFormView(FormView):
    template_name = 'Users/login.html'
    form_class = forms.LoginForm
    success_url =reverse_lazy('app_home:home-add')

    def form_valid(self, form):
        us = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request,us)
        return super(LoginFormView, self).form_valid(form)

@login_required
def logout_(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('app_user:user-login'))