from django import forms
from .models import Recipe, Ingredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'recipe_tag','prep_time','cook_time')

#IngredientFormSet = inlineformset_factory(Recipe, Ingredient, form=RecipeForm, extra=1)

class IngredientForm(forms.ModelForm):		
	class Meta:
		model = Ingredient
		fields = ('ingredient_name', 'ingredient_quantity', 'quantity_type')
		