from .forms import LoginUserForm
from django.contrib.auth.views import LoginView


class LoginUser(LoginView): # Авторизация
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    # def get_success_url(self):
    #     return reverse_lazy('home')


