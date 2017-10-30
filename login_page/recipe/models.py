# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	def __str__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text


class Recipe(models.Model):
	recipe_name = models.CharField(max_length=200)
	recipe_tag = models.CharField(max_length=200)
	prep_time = models.IntegerField(default=0)
	cook_time = models.IntegerField(default=0)

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

class Ingredient(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	null=True
	ingredient_name = models.CharField(max_length=200)
	ingredient_quantity = models.DecimalField(max_digits=5, decimal_places=2)
	quantity_type = models.CharField(max_length=200)

	def __str__(self):
		return self.ingredient_name

	def quantity(self):
		return str(self.ingredient_quantity) + " " + self.quantity_type

	def details(self):
		return self.ingredient_name, self.ingredient_quantity, self.quantity_type