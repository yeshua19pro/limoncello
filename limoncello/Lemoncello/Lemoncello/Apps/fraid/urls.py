from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from Lemoncello.Apps.fraid.views import *
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^usuarios', users, name='usuarios'),
	url(r'^miperfil', perfil, name='miperfil'),
	url(r'^miscursos', misCursos, name='miscursos'),
	url(r'^curso-info', misCursos, name='curso-info'),
	url(r'^login', LoginView.as_view(template_name='login.html'), name='login'),
	url(r'^logout', LogoutView.as_view(template_name='login.html'), name='logout'),
]