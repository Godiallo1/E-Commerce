from django.shortcuts import render
from . models import*

# Create your views here.

def products(request):
    products = Products.objects.all()
    if products:
        context = {"products":products}
        return render(request, 'products_page.html', context)