from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from .models import Recipe

# Create your views here.
def home (request):
	return render(request, 'homepage/home.html')
	
def recipes(request):
	recipe = get_object_or_404(Recipe, pk=1)
	# ingredient = get_object_or_404(Ingredient, pk=recipe_id)

	# return render(request, 'polls/test.html', {'recipe': recipe})
	return render(request, 'polls/test.html', {'recipe': recipe})

def shopping_list(request):
	return render(request, 'homepage/shopping_list.html')