from django.urls import path
from . import views


urlpatterns = [
	path('home', views.home),
	path('szerverrol', views.szerverrol),
	path('csapat', views.csapat),
	path('discord', views.discord),
]