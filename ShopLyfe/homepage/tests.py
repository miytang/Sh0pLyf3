from django.test import TestCase
import views

def runUnitTests():
	addRecipeTest()
	addIngredientTest()
	addToListTest()
	removeFromListTest()
	deleteRecipeTest()

# all unit tests need inputs and outputs

# inputs POST request

# add pesto recipe
# ingredients basil, pine nuts, olive oil

# add turkey recipe
# ingredients turkey, salt, pepper
def addRecipeTest():
	print("I am testing add_recipe")

# add parmesan cheese and green onions to pesto recipe
# add cheese cloth and truffle oil to turkey recipe
def addIngredientTest():
	print("I am testing add_ingredient")

# increase pesto recipe amount by 5
# increase the turkey recipe amount by 25
def addToListTest():
	print("I am testing add_to_list")

# decrease the pesto amount by 3
# decrese the turkey amount by 9
def removeFromListTest():
	print("I am testing remove_from_list")

# delete petso recipe
# delete turkey recipe
def deleteRecipeTest():
	print("I am testing delete_recipe")

runUnitTests()