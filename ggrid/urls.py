from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("<int:shelf_id>/", views.shelf, name="shelf"),
	path("complete/", views.complete, name="complete"),
	path("gen_images/", views.gen_images, name="gen_images")
]