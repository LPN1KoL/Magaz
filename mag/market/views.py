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

def admin_test(request):
	if request.user.role.admin_access:
		return HttpResponseRedirect('myadmin/main')
	else:
		return HttpResponseRedirect('/home')

def home(request):
	return render(request, 'home.html')

def admin_main(request):
	return render(request, 'admin_main.html')

def myadmin_categories(request):
	if request.user.role.admin_access:
		categories = Category.objects.all()
		return render(request, 'myadmin_categories.html', {'categories': categories})
	else:
		return HttpResponseRedirect('/home')

def myadmin_tags(request):
	if request.user.role.admin_access:
		tags = Tag.objects.all()
		return render(request, 'myadmin_tags.html', {'tags': tags})
	else:
		return HttpResponseRedirect('/home')

def myadmin_products(request):
	if request.user.role.admin_access:
		products = Product.objects.all()
		return render(request, 'myadmin_products.html', {'products': products})
	else:
		return HttpResponseRedirect('/home')

def myadmin_orders(request):
	if request.user.role.admin_access:
		orders = Order.objects.all()
		return render(request, 'myadmin_orders.html', {'orders': orders})
	else:
		return HttpResponseRedirect('/home')

def admin_add_product(request):
	if request.user.role.admin_access:
		if request.method == 'GET':
			tags = Tag.objects.all()
			categories = Category.objects.all()
			return render(request, 'admin_add_product.html', {'tags': tags, 'categories': categories})
		else:
			name = request.POST["name"]
			price = request.POST["price"]
	else:
		return HttpResponseRedirect('/home')