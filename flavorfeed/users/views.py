from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class LoginUser(LoginView): # Авторизация
    form_class = LoginUserForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('home')


class RegisterUser(CreateView): # Регистрация
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
