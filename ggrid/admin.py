from django.contrib import admin

# Register your models here.

from .models import Section, Shelf, Category, Item, Cart, CartItem, KeyStroke

admin.site.register(Section)
admin.site.register(Shelf)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(KeyStroke)