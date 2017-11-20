from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm
from django.forms.formsets import formset_factory

from django.contrib.auth.models import User
# Create your views here.

# View for listing the recipes you currently have
# passes in the context, latest_recipe_list which 
# holds all the recipe objects (models).
class RecipesView(generic.ListView):
	template_name = 'homepage/recipes.html'
	# Sets the name of the context as 'latest_recipe_list'
	context_object_name = 'latest_recipe_list'
	# This grabs the context
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

# Maybe make another page after making a recipe to keep adding ingredients or something...
# redirect('add_ingredients_view') or something
# then use another form for it.
def add_recipe(request):
	IngredientFormSet = formset_factory(IngredientForm, can_delete=True)
	user = request.user
	if request.method == 'POST':
		# Grab recipe form and ingredients formset
		recipe_form = RecipeForm(request.POST)
		ingredient_formset = IngredientFormSet(request.POST)
		# Make sure we have a valid form
		if recipe_form.is_valid() and ingredient_formset.is_valid():
			# Save data into recipe form
			new_recipe = recipe_form.save(commit=False)
			new_recipe.user = user
			recipe_name = recipe_form.cleaned_data.get('recipe_name')
			recipe_tag = recipe_form.cleaned_data.get('recipe_tag')
			prep_time = recipe_form.cleaned_data.get('prep_time')
			cook_time = recipe_form.cleaned_data.get('cook_time')
			new_recipe.save()
			
			# Save ingredients data into each ingredients form in formset
			# ingredients = []
			for ingredient_form in ingredient_formset:
				new_ingredient = ingredient_form.save(commit=False)
				new_ingredient.recipe = new_recipe
				ingredient_name = ingredient_form.cleaned_data.get('ingredient_name')
				ingredient_amount = ingredient_form.cleaned_data.get('ingredient_amount')
				quantity_type = ingredient_form.cleaned_data.get('quantity_type')
				new_ingredient.save()
			if 'add' in request.POST:
				return redirect('add_ingredient', new_recipe.id)
			if 'done' in request.POST:
				return redirect('recipes_view')
	else:
		recipe_form = RecipeForm()
		ingredient_formset = IngredientFormSet()
	
	context = {
		'recipe_form': recipe_form,
		'ingredient_formset': ingredient_formset,
	}
	return render(request, 'homepage/recipe_form.html', context)
	
# need to pass in recipe ID
def add_ingredient(request, recipe_id):
	if request.method == 'POST':
		recipe_record = get_object_or_404(Recipe, pk=recipe_id)
		ingredient_form = IngredientForm(request.POST)
		if ingredient_form.is_valid():
			new_ingredient = ingredient_form.save(commit=False)
			new_ingredient.recipe = recipe_record
			ingredient_name = ingredient_form.cleaned_data.get('ingredient_name')
			ingredient_amount = ingredient_form.cleaned_data.get('ingredient_amount')
			quantity_type = ingredient_form.cleaned_data.get('quantity_type')
			new_ingredient.save()
			
			if 'more' in request.POST:
				return redirect('add_ingredient', recipe_id)
			elif 'done' in request.POST:
				return redirect('recipes_view')
	else:
		ingredient_form = IngredientForm()
	return render(request, 'homepage/ingredient_form.html', {'ingredient_form': ingredient_form})
	
def add_to_list(request, recipe_id):
	query = Recipe.objects.get(pk=recipe_id)
	#ingredient_list = Ingredient.objects.get(pk=query)
	query.recipe_amount += 1
	
	#for ingredient in ingredient_list
	#	ingredient.ingredient_quantity *= query.recipe_amount
	
	query.save()
	return redirect ('recipes_view')

def remove_from_list(request, recipe_id):
	query = Recipe.objects.get(pk=recipe_id)
	query.recipe_amount -= 1
	query.save()
	return redirect ('recipes_view')

def delete_recipe(request, recipe_id):
	query = Recipe.objects.get(pk=recipe_id)
	query.delete()
	return redirect ('recipes_view')