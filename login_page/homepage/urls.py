from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
	url(r'^recipes/(?P<recipe_id>[0-9]+)/$', views.recipes, name='recipes'),
	url(r'^shopping_list/$', views.shopping_list, name='shopping_list'),
]