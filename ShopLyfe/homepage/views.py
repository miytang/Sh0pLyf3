from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    return HttpResponse("Hello, this is your homepage.")


def recipes(request):
    return HttpResponse("This is your recipes.")


def shopping_list(request):
    return HttpResponse("Here is your shopping list.")