from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)

def search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(product_name__icontains=query) if query else []
    context = {'products': products, 'query': query}
    return render(request, 'index.html', context)