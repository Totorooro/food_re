from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import LoginUserForm
from django.contrib.auth.views import LoginView


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    return HttpResponse("logout")