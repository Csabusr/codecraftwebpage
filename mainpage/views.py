from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
	return render(request, 'mainpage/main.html')

def szerverrol(request):
	return render(request, 'mainpage/szerverrol.html')

def cv(request):
	return render(request, 'mainpage/cv.html')

def viewer(request):
	return render(request, 'mainpage/viewer.html')


