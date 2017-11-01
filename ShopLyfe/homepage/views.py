from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Recipe

# Create your views here.

# View for listing the recipes you currently have
# passes in the context, latest_recipe_list which 
# holds all the recipe objects (models).
class RecipesView(generic.ListView):
	template_name = 'homepage/recipes.html'
	context_object_name = 'latest_recipe_list'
	def get_queryset(self):
		return Recipe.objects.order_by('id')
		
# View for listing all the ingredients from your
# recipe list.
# Uses pretty much same logic as recipesview.	
class ShoppingListView(generic.ListView):		
	template_name = 'homepage/shopping_list.html'
	context_object_name = 'latest_recipe_list'
	def get_queryset(self):
		return Recipe.objects.order_by('id')

# For dispaying homepage.
def home (request):
	return render(request, 'homepage/home.html')

# For displaying the recipe form.
def recipe_form (request):
	return render(request, 'homepage/recipe_form.html')

# For displaying the specific recipe details
# From RecipesView, if you click on any recipe, it will
# pass in the recipe_id based off the respective recipe
# clicked and then load this page.	
def recipes(request, recipe_id):
	recipe = get_object_or_404(Recipe, pk=recipe_id)
	return render(request, 'homepage/recipe_details.html', {'recipe': recipe})

# For displaying the ingredients list
# Use ShoppingListView instead since this
# is less "django"-ey.
"""def shopping_list(request):
	recipe_list = Recipe.objects.order_by('id')
	return render(request, 'homepage/shopping_list.html', {'recipe_list': recipe_list})"""