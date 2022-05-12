from django.shortcuts import render
import products.forms
from products.models import Product, OrderInformation
from django.shortcuts import get_object_or_404
from .filters import ProductFilter
from formtools.wizard.views import SessionWizardView



FORMS = [("address", products.forms.CheckoutForm1),
         ("cc", products.forms.CheckoutForm2),
         ("review", products.forms.CheckoutForm3)]

TEMPLATES = {"0": "products/checkout1.html",
             "1": "products/checkout2.html",
             "2": "products/checkout3.html"}

def index(request):
    products = Product.objects.all()
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs
    return render(request, 'products/index.html',
                  {'products': products, 'myFilter': myFilter
    })

def index_by_name(request):
    products = Product.objects.all().order_by('name')
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


class CheckoutWizard(SessionWizardView):
    def get_context_data(self, form, **kwargs):
        context = super(CheckoutWizard, self).get_context_data(form=form, **kwargs)
        if self.steps.current == '2':
            context.update({'all_data': self.get_all_cleaned_data()})
        return context

    # def get_form_initial(self, step):
    #     current_step = self.storage.current_step
    #     # get the data for step 1 on step 3
    #     if current_step == '2':
    #         prev_data = self.storage.get_step_data('0')
    #
    #         prev_data1 = self.storage.get_step_data('1')
    #
    #         # some_var = prev_data1.get('0-name', '')
    #
    #         return self.initial_dict.get(step, prev_data1)
    #
    #     return self.initial_dict.get(step, {})

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, form_dict, **kwargs):
        data = [form.cleaned_data for form in form_list]
        order_info = OrderInformation()
        order_info.name = data[0]['name']
        order_info.address = data[0]['address']
        order_info.address2 = data[0]['address2']
        order_info.city = data[0]['city']
        order_info.country = data[0]['country']
        order_info.zip = data[0]['zip']
        order_info.cardholder = data[1]['cardholder']
        order_info.cardnumber = data[1]['cardnumber']
        order_info.exp = data[1]['exp']
        order_info.cvc = data[1]['cvc']
        order_info.save()
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list]
        })
