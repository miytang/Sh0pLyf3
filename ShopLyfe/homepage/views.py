from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm
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
	
# Maybe make another page after making a recipe to keep adding ingredients or something...
# redirect('add_ingredients_view') or something
# then use another form for it.
def add_recipe(request):
	if request.method == 'POST':
		recipe_form = RecipeForm(request.POST)
		if recipe_form.is_valid(): #and ingredients_form.is_valid():
			new_recipe = recipe_form.save(commit=False)
			recipe_name = recipe_form.cleaned_data.get('recipe_name')
			recipe_tag = recipe_form.cleaned_data.get('recipe_tag')
			prep_time = recipe_form.cleaned_data.get('prep_time')
			cook_time = recipe_form.cleaned_data.get('cook_time')
			new_recipe.save()
			return redirect('add_ingredient', new_recipe.id)
	else:
		recipe_form = RecipeForm()
		
	return render(request, 'homepage/recipe_form.html', {'recipe_form': recipe_form})
	
# need to pass in recipe ID
def add_ingredient(request, recipe_id):
	#my_record = MyModel.objects.get(id=XXX)
	#form = MyModelForm(instance=my_record)
	if request.method == 'POST':
		recipe_record = get_object_or_404(Recipe, pk=recipe_id)
		ingredient_form = IngredientForm(request.POST, instance=recipe_record)
		if ingredient_form.is_valid():
			new_ingredient = ingredient_form.save(commit=False)
			recipe = ingredient_form.cleaned_data.get('recipe')
			ingredient_name = ingredient_form.cleaned_data.get('ingredient_name')
			ingredient_amount = ingredient_form.cleaned_data.get('ingredient_amount')
			quantity_type = ingredient_form.cleaned_data.get('quantity_type')
			new_ingredient.save()
			return redirect('recipes_view')
	else:
		ingredient_form = IngredientForm()
	return render(request, 'homepage/ingredient_form.html', {'ingredient_form': ingredient_form})