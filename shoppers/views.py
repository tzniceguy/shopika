from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)
        if user is not None:
            messages.success(request, "Successful Login, Redirect")
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invaild credentials provided")
    return render(request, 'authentication.html')


def services(request):
    return render(request, 'index.html')

def product_list(request):
    search_query = request.GET.get('search-box')
    if search_query:
        products = Product.objects.filter(name__icontains=search_query)
    else:
        products = Product.objects.all()
    return render(request, 'product-list.html', {'products': products})

def product_detail(request, pk):
    product= get_object_or_404(Product, pk = pk )
    return render(request, 'product-detail.html', {'product': product})