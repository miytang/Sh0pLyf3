from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='homepage/home.html'), name='home'),
	url(r'^recipes/$', views.recipes, name='recipes'),
	url(r'^shopping_list/$', views.shopping_list, name='shopping_list'),
]