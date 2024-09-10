from django.shortcuts import render
from .models import ProductakhorModel

# Create your views here.
def show_main(request):
    model = ProductakhorModel.objects.all()

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
    }

    return render(request, "main.html", context)