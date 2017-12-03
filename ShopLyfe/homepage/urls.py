from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
	url(r'^recipes/$', views.RecipesView.as_view(), name='recipes_view'),
	url(r'^recipes/form/$', views.add_recipe, name='add_recipe'),
	url(r'^recipes/form/add_ingredient/(?P<recipe_id>[0-9]+)/$', views.add_ingredient, name='add_ingredient'),
	url(r'^recipes/(?P<recipe_id>[0-9]+)/$', views.recipes, name='recipes'),
	url(r'^shopping_list/$', views.ShoppingListView.as_view(), name='shopping_list'),
	url(r'^add_to_list/(?P<recipe_id>[0-9]+)/$', views.add_to_list, name='add_to_list'),
	url(r'^remove_from_list/(?P<recipe_id>[0-9]+)/$', views.remove_from_list, name='remove_from_list'),    
	url(r'^delete_recipe/(?P<recipe_id>[0-9]+)/$', views.delete_recipe, name='delete_recipe'),   
]