from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home (request):
	return render(request, 'homepage/home.html')
	
def recipes(request):
    return render(request, 'homepage/recipes.html')
	
def shopping_list(request):
    return render(request, 'homepage/shopping_list.html')