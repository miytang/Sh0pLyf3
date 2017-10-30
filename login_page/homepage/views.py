from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Recipe

# Create your views here.
def homepage(request):
	return HttpResponse("Hello, this is your homepage.")
	
def recipes(request, recipe_id):
	# return HttpResponse("This is your recipes.")
	recipe = get_object_or_404(Recipe, pk=recipe_id)
	# ingredient = get_object_or_404(Ingredient, pk=recipe_id)

	return render(request, 'polls/test.html', {'recipe': recipe})
	
def shopping_list(request):
	return HttpResponse("Here is your shopping list.")