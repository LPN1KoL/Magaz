from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *


def welcome(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login')
    else:
        return HttpResponseRedirect('/home')

def login_view(request):
	if request.method == 'POST':
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/')
	return render(request, 'login.html')





def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')


def register_view(request):
	form = RegForm()
	if request.method == 'POST':
		username = request.POST["username"]
		password = request.POST["password"]
		usr = User.objects.create_user(username=username, password=password)
		usr.save()
		login(request, usr)
		return HttpResponseRedirect('/')
	return render(request, 'register.html', {'form': form})

def get_search(request):
	if request.method == "GET":
		products = [x.to_json() for x in Product.objects.all()]
		return JsonResponse({'products': products})