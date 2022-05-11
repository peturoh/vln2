from django.shortcuts import render

import products.forms
from products.models import Product
from django.shortcuts import get_object_or_404
from .filters import ProductFilter
from formtools.wizard.views import SessionWizardView

FORMS = [("address", products.forms.CheckoutForm1),
         ("cc", products.forms.CheckoutForm2)]

TEMPLATES = {"0": "products/checkout1.html",
             "1": "products/checkout2.html"}

def index(request):
    products = Product.objects.all()
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs
    return render(request, 'products/index.html',
                  {'products': products, 'myFilter': myFilter
    })

def create(request):
    return render(request, 'products/create_product.html')

def get_product_by_id(request, id):
    return render(request, 'products/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })

def order_by_name(request):
    products = Product.objects.all().order_by('name')
    return render(request, 'products/index.html', {
        'product': products
    })

class CheckoutWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
