from django.urls import path
from . import views


urlpatterns = [
	path('', views.home),
	path('szerverrol', views.szerverrol),
	path('csapat', views.csapat),
	path('discord', views.discord),
	path('munkak', views.munkak),
	path('rangok', views.rangok),
	path('parancsok', views.parancsok),
	path('helyek', views.helyek),
]