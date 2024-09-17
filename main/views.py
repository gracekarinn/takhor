from django.shortcuts import render
from .models import ProductakhorModel
from django.shortcuts import render, redirect
from main.forms import ProductForm
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    product_entries = ProductakhorModel.objects.all()

    product = [
        {
            "name": "Cake Chocolate",
            "price": 100,
            "description": "A delightfully squishy cake-shaped toy that's as soft as it is sweet.",
            "image": "cake.jpg",
            "quantity": 10
        },
        {
            "name": "Banana Squish",
            "price": 200,
            "description": "Go bananas for this fruity squishy!",
            "image": "/banana.jpg",
            "quantity": 20
        },
        {
            "name": "Cherry Squeezy",
            "price": 300,
            "description": "A cherry-licious squishy",
            "image": "cherry.jpg",
            "quantity": 30
        }
    ]

    context = {
        'name': 'Grace Karina',
        'NPM' : '2306275834',
        'class' : 'PBP F',
        'shop': 'takhor',
        'product': product,
        'product_entries': product_entries
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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