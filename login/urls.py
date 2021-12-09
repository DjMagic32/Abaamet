from django.urls.conf import path
from django.contrib.auth.decorators import login_required
from .views import LoginFormView, logoutUsuario

urlpatterns = [
    path('',LoginFormView.as_view(),name='loginPath'),
    path('logout/',login_required(logoutUsuario),name='logoutPath'),

]