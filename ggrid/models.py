from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Cart(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def summary(self):
		cart_summ = {}
		for item in CartItem.objects.filter(cart=self):
			if item.category.id in cart_summ:
				cart_summ[item.category.id][2] += 1
			else:
				cart_summ[item.category.id] = [item.category.name, '{:.2f}'.format(item.category.price), 1]
		return cart_summ

	def total(self):
		total = 0
		for item in CartItem.objects.filter(cart=self):
			total += item.category.price
		return total

	def __str__(self):
		return self.user.first_name + "'s Cart"

class Section(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Shelf(models.Model):
	name = models.CharField(max_length=200)
	section = models.ForeignKey(Section, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=200)
	shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
	price = models.FloatField(default=1.99)
	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=300)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class CartItem(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	def __str__(self):
		return self.category.name + "_" + self.cart.user.last_name

class KeyStroke(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

class Recipe(models.Model):
	name = models.CharField(max_length=300)
	shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class Ingredient(models.Model):
	amount = models.IntegerField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	def __str__(self):
		return self.category.name

