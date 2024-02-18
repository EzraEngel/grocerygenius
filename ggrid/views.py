from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .models import Category, Shelf, Cart, CartItem, KeyStroke, Section
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import random as rd
import requests
import shutil
import time

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
		shelf = Shelf.objects.get(pk=shelf_id)
		section_id = shelf.section.id
		previous_section = section_id-1

		if previous_section < 1:
			previous_section = 1
		previous_shelf = Shelf.objects.filter(section=previous_section).first().id

		next_section = section_id + 1
		if next_section > 10:
			next_shelf = 999
		else:
			next_shelf = Shelf.objects.filter(section=next_section).first().id
		category_grid = []
		for i, c in enumerate(category_list):
			if i%3 == 0:
				category_grid.append([])
			category_grid[int(i/3)].append((c,i+1))
		context = {
			"category_grid": category_grid,
			"shelf": Shelf.objects.get(pk=shelf_id),
			"shelf_count": shelf_count,
			"cart_dict": request.user.cart.summary(),
			"cart_tot": '{:.2f}'.format(request.user.cart.total()),
			"next_shelf": next_shelf,
			"previous_shelf": previous_shelf
		}
	return render(request, "shelf.html", context)

def complete(request):
	context={}
	return render(request, "complete.html", context)

def fetch_image(query, pk):
	try:
	    url = "https://api.unsplash.com/search/photos"
	    params = {
	        "query": query,
	        "client_id": "y3RuxbSYYarspf4h0Tq9VBedG7Og0qWXS_TKUEFj1-Q"
	    }
	    response = requests.get(url, params=params).json()
	    print(response)
	    image_url = response['results'][0]['urls']['regular']

	    # Download and save the image
	    response = requests.get(image_url, stream=True)
	    with open('media/'+str(pk)+'.jpg', 'wb') as out_file:
	        shutil.copyfileobj(response.raw, out_file)
	    del response

	except:
		pass


def gen_images(request):
	# for category in Category.objects.all()[24:43]:
	#     time.sleep(1)
	#     fetch_image(category.name, category.id)
	return HttpResponse("You're not supposed to be here.")