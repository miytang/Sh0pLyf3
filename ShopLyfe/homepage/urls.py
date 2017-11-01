from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
	url(r'^recipes/$', views.RecipesView.as_view(), name='recipes_view'),
	url(r'^recipes/form/$', views.recipe_form, name='recipe_form'),
	url(r'^recipes/(?P<recipe_id>[0-9]+)/$', views.recipes, name='recipes'),
	url(r'^shopping_list/$', views.ShoppingListView.as_view(), name='shopping_list'),
]