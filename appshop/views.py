from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    appshop = Product.object.all()
    return render(request, 'index.html', {"appshop": appshop})


def Blog(request):
    return render(request, 'Blog.html', {"appshop": Blog})


def Offer(request):
    return render(request, 'offer.html', {"appshop": Offer})

# Create your views here.
