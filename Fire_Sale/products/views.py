from django.shortcuts import render
from products.models import Product
from django.shortcuts import get_object_or_404
from .filters import ProductFilter

# Create your views here.


def index(request):
    products = Product.objects.all().order_by('name')
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs
    context = {'products': products, 'myFilter': myFilter}
    return render(request, 'products/index.html', context) #context={'products': products}


def get_product_by_id(request, id):
    return render(request, 'products/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })

