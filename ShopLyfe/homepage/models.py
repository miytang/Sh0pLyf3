from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Recipes model
# Can make a form from this, probably
class Recipe(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	recipe_name = models.CharField(max_length=200)
	recipe_tag = models.CharField(max_length=200)
	prep_time = models.IntegerField(default=0)
	cook_time = models.IntegerField(default=0)
	recipe_amount = models.IntegerField(default=0)
	
	def __str__(self):
		return self.recipe_name
	def tag(self):
		return self.recipe_tag
	def p_time(self):
		return self.prep_time
	def c_time(self):
		return self.cook_time
	def r_amount(self):
		return self.recipe_amount  
	def details(self):
		return self.recipe_name, self.recipe_tag, self.prep_time, self.cook_time, self.recipe_amount

# Ingredients model
# Each ingredient belongs to a recipe
# Can the same ingredient belong to multiple recipes???
class Ingredient(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank = True, null = True)
	ingredient_show = models.BooleanField(default=True)
	ingredient_name = models.CharField(max_length=200, null = True)
	ingredient_quantity = models.DecimalField(max_digits=5, decimal_places=2, default = '0.0', null = True)
	quantity_type = models.CharField(max_length=200, null = True)

	def __str__(self):
		return self.ingredient_name
	def quantity(self):
		return str(self.ingredient_quantity) + " " + self.quantity_type
	def details(self):
		return self.ingredient_name, self.ingredient_quantity, self.quantity_type
	def total(self):
		return self.recipe.recipe_amount*self.ingredient_quantity