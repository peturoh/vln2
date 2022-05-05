from django.shortcuts import render
from products.models import Product
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'products/index.html', context) #context={'products': products}


def get_product_by_id(request, id):
    return render(request, 'products/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })

