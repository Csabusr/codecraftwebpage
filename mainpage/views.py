from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
	return render(request, 'mainpage/main.html')

def szerverrol(request):
	return render(request, 'mainpage/szerverrol.html')

def csapat(request):
	return render(request, 'mainpage/codecraft_csapat.html')

def discord(request):
	return render(request, 'mainpage/discord.html')

def munkak(request):
	return render(request, 'mainpage/info.html')

def rangok(request):
	return render(request, 'mainpage/info.html')

def parancsok(request):
	return render(request, 'mainpage/info.html')

def helyek(request):
	return render(request, 'mainpage/info.html')


