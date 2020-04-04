from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    appshop = Product.object.all()
    return render(request, 'index.html', {"appshop": appshop})


def new(request):
    return HttpResponse("new products")


def Offer(request):
    return render(request, 'offer.html', {"appshop": Offer })

# Create your views here.
