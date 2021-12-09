from django.http.response import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls.base import reverse_lazy

class LoginFormView(LoginView):
    template_name = 'login.html'

def logoutUsuario (request):
    logout (request)
    return HttpResponseRedirect(reverse_lazy("loginPath"))