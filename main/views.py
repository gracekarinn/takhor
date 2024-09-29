from django.shortcuts import render, redirect, get_object_or_404
from .models import ProductakhorModel
from main.forms import ProductForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    last_login = request.COOKIES.get('last_login')
    product_entries = ProductakhorModel.objects.filter(user=request.user)

    product = [
        {
            "name": "Cake Chocolate",
            "price": 100,
            "description": "A delightfully squishy cake-shaped toy that's as soft as it is sweet.",
            "image": "/images/kue.jpg",
            "quantity": 10
        },
        {
            "name": "Banana Squish",
            "price": 200,
            "description": "Go bananas for this fruity squishy!",
            "image": "/images/banana.jpg",
            "quantity": 20
        },
        {
            "name": "Cherry Squeezy",
            "price": 300,
            "description": "A cherry-licious squishy",
            "image": "/images/cherry.jpg",
            "quantity": 30
        }
    ]

    context = {
        'name': request.user.username,
        'NPM' : '2306275834',
        'class' : 'PBP F',
        'shop': 'takhor',
        'product': product,
        'product_entries': product_entries,
        'last_login': last_login
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()
            return redirect('main:show_main')
    else:
        form = ProductForm()
    
    context = {'form': form}
    return render(request, 'create_product_entry.html', context)

def show_xml(request):
    product_entries = ProductakhorModel.objects.all()
    data = serializers.serialize('xml', product_entries)
    return HttpResponse(data, content_type='application/xml')

def show_json(request):
    product_entries = ProductakhorModel.objects.all()
    data = serializers.serialize('json', product_entries)
    return HttpResponse(data, content_type='application/json')

def show_xml_by_id(request, id):
    product_entries = ProductakhorModel.objects.get(id=id)
    data = serializers.serialize('xml', [product_entries])
    return HttpResponse(data, content_type='application/xml')

def show_json_by_id(request, id):
    product_entries = ProductakhorModel.objects.get(id=id)
    data = serializers.serialize('json', [product_entries])
    return HttpResponse(data, content_type='application/json')

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
      else:
            messages.error(request, 'Invalid username or password.')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product_entry(request, id):
    product_entry = ProductakhorModel.objects.get(pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product_entry)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        form = ProductForm(instance=product_entry)
    context = {'form': form, 'product_entry': product_entry}
    return render(request, 'edit_product_entry.html', context)

def delete_product_entry(request, id):
    product_entry = ProductakhorModel.objects.get(pk=id)
    product_entry.delete()
    return HttpResponseRedirect(reverse('main:show_main'))