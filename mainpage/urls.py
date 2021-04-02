from django.urls import path
from . import views


urlpatterns = [
	path('', views.home),
	path('szerverrol/', views.szerverrol),
	path('cv/', views.cv),
	path('viewer/', views.viewer),


]