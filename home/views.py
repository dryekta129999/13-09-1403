from django.shortcuts import render
from .models import *


# Create your views here.

def home(request):
    category = Category.objects.filter(sub_cat=False)
    return render(request , 'home/home.html',{'category':category})

def all_product(request,slug=None,id=None):
    products = Product.objects.all()
    category = Category.objects.filter(sub_cat=False)
    if slug and id:
        data = Category.objects.get(slug = slug , id=id)
        products = products.filter(category = data)
    return render(request , 'home/products.html' ,{'products':products,'category':category})


def product_detail(request , id):
    product = Product.objects.get(id = id)
    return render(request ,'home/detail.html' , {'product':product})



