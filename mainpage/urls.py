from django.urls import path
from . import views


urlpatterns = [
	path('', views.home),
	path('aboutme/', views.about_me),
	path('cv/', views.cv),
	path('viewer/', views.viewer),


]