from django.shortcuts import render
from .models import ProductakhorModel

# Create your views here.
def show_main(request):
    model = ProductakhorModel.objects.all()

    product = [
        {
            "name": "Apple",
            "price": 100,
            "description": "This is an apple",
            "image": "images/apple.jpg",
            "quantity": 10
        },
        {
            "name": "Banana",
            "price": 200,
            "description": "This is a banana",
            "image": "images/banana.jpg",
            "quantity": 20
        },
        {
            "name": "Cherry",
            "price": 300,
            "description": "This is a cherry",
            "image": "images/cherry.jpg",
            "quantity": 30
        }
    ]

    context = {
        'name': 'Grace Karina',
        'NPM' : '2306275834',
        'class' : 'PBP F',
        'shop': 'takhor',
        'product': product,
    }

    return render(request, "main.html", context)