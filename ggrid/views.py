from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .models import Category, Shelf, Cart, CartItem, KeyStroke
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import random as rd

# Create your views here.

def index(request):
	if request.method=='POST':
		username = str(rd.randrange(100000000))
		password = 'defaultpassword'
		user = User.objects.create_user(username=username, password=password)
		user.save()
		Cart.objects.create(user=user)
		if request.user.is_authenticated:
			logout(request)
		login(request, user)
		return HttpResponseRedirect(reverse('shelf', args=[1]))
	context={}
	return render(request, "index.html", context)

def shelf(request, shelf_id):
	if request.method == 'POST':
		action = request.POST.get('action')
		category_id = request.POST.get('category_id')
		user_cart, _ = Cart.objects.get_or_create(user=request.user)
		category = get_object_or_404(Category, id=category_id)
		print('ping')

		if action == 'CREATE':
			CartItem.objects.create(cart=user_cart, category=category)
			return JsonResponse({'status': 'Item added to cart'})
		elif action == 'DELETE':
			items = CartItem.objects.filter(cart=user_cart, category=category)
			if items.exists():
				items.first().delete()
				return JsonResponse({'status': 'Item removed from cart'})
			else:
				return JsonResponse({'status': 'Item not found in cart'}, status=404)
		elif action == 'KEYSTROKE':
			KeyStroke.objects.create(user=request.user)
			return JsonResponse({'status': 'Keystroke recorded'})

		return JsonResponse({'status': 'Invalid action'}, status=400)
	else:
		if not Shelf.objects.filter(pk=shelf_id).exists():
			return HttpResponseRedirect(reverse('complete'))
		shelf_count = Shelf.objects.all().count()
		category_list = Category.objects.filter(shelf=shelf_id)
		category_grid = []
		for i, c in enumerate(category_list):
			if i%4 == 0:
				category_grid.append([])
			category_grid[int(i/4)].append((c,i+1))
		context = {
			"category_grid": category_grid,
			"shelf": Shelf.objects.get(pk=shelf_id),
			"shelf_count": shelf_count,
			"cart_dict": request.user.cart.summary(),
			"cart_tot": '{:.2f}'.format(request.user.cart.total())
		}
	return render(request, "shelf.html", context)

def complete(request):
	context={}
	return render(request, "complete.html", context)