from django.db import models

# Create your models here.


class Recipe(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	recipe_name = models.CharField(max_length=200)
	recipe_tag = models.CharField(max_length=200)
	prep_time = models.IntegerField(default=0)
	cook_time = models.IntegerField(default=0)

	# def __init__(self, recipe_name, recipe_tag, prep_time, cook_time, ingredient_set):
	# 	r = Recipe(recipe_name = recipe_name, recipe_tag = recipe_tag, prep_time = prep_time, cook_time = cook_time, ingredient_set = ingredient_set)
	# 	return r

	def __str__(self):
		return self.recipe_name

	def tag(self):
		return self.recipe_tag

	def p_time(self):
		return self.prep_time

	def c_time(self):
		return self.cook_time

	def details(self):
		return self.recipe_name, self.recipe_tag, self.prep_time, self.cook_time

	# def addIngredient(self, ingredient_name, ingredient_quantity, quantity_type):
	# 	self.ingredient_set.create()

class Ingredient(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True, null=True)
	null=True
	ingredient_name = models.CharField(max_length=200)
	ingredient_quantity = models.DecimalField(max_digits=5, decimal_places=2)
	quantity_type = models.CharField(max_length=200)

	# def __init__(self, ingredient_name, ingredient_quantity, quantity_type):
	# 	self.recipe = recipe
	# 	self.ingredient_name = ingredient_name
	# 	self.ingredient_quantity = ingredient_quantity
	# 	self.quantity_type = quantity_type

	def __str__(self):
		return self.ingredient_name

	def quantity(self):
		return str(self.ingredient_quantity) + " " + self.quantity_type

	def details(self):
		return self.ingredient_name, self.ingredient_quantity, self.quantity_type