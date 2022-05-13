from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
import products.forms
from products.models import Product, OrderInformation, ProductImage, ProductOffer
from django.shortcuts import get_object_or_404
from products.forms import CreateItemForm
from formtools.wizard.views import SessionWizardView


FORMS = [("address", products.forms.CheckoutForm1),
         ("cc", products.forms.CheckoutForm2),
         ("review", products.forms.CheckoutForm3)]

TEMPLATES = {"0": "products/checkout1.html",
             "1": "products/checkout2.html",
             "2": "products/checkout3.html"}


def index(request):

    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']

        products_filter = [{
            'id': x.id,
            'firstImage': x.productimage_set.first().image,
            'name': x.name,
            'description': x.description
        } for x in Product.objects.filter(name__icontains=search_filter)]

        if 'sort_by' in request.GET:
            sort_by = request.GET['sort_by']
            if sort_by == '1':
                sorted_list = sorted(products_filter, key=lambda d: d['name'])
                return JsonResponse({'data': sorted_list, 'search': search_filter})
            else:
                return JsonResponse({'data': products_filter, 'search': search_filter})
        else:
            return JsonResponse({'data': products_filter, 'search': search_filter})

    else:

        if 'sort_by' in request.GET:
            sort_by = request.GET['sort_by']
            products_filter = [{
                'id': x.id,
                'firstImage': x.productimage_set.first().image,
                'name': x.name,
                'description': x.description
            } for x in Product.objects.all()]

            if sort_by == '1':
                sorted_list = sorted(products_filter, key=lambda d: d['name'])
                return JsonResponse({'data': sorted_list})
            else:
                return JsonResponse({'data': products_filter})

    return render(request, 'products/index.html',
                  {'products': Product.objects.all()})


@login_required
def get_my_listings(request):
    # my_products = Product.objects.filter(seller_id=request.user)

    my_listings = [{
        'id': x.id,
        'firstImage': x.productimage_set.first().image,
        'name': x.name,
        'description': x.description
    } for x in Product.objects.filter(seller_id=request.user)]

    for listing in my_listings:

        bids = ProductOffer.objects.filter(product_id=listing['id'])
        if bids:
            listing['all_bids'] = [{
                'bid': x.id,
                'bidder': x.bidder_id,
                'amount': int(x.offer_amount)
            } for x in bids]
        else:
            listing['all_bids'] = []

    return render(request, 'products/my_listings.html',
                  {'my_listings': my_listings})

@login_required
def create(request):
    if request.method == 'POST':
        form = CreateItemForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            product_image = ProductImage(image=request.POST['image'], product=product)
            product_image.save()
            return redirect('/')
    else:
        form = CreateItemForm()
    return render(request, 'products/create_product.html', {
        'form': form
    })


def get_product_by_id(request, id):

    if request.method == 'POST':

        bid_amount = request.POST.get('bid_amount')

        if bid_amount != '':
            bid_status = place_bid(id, request.user, float(bid_amount))
            return JsonResponse({'bid_status': bid_status, 'highest_bid': int(get_highest_bid(id))})

        else:
            print('Please enter an amount to bid')

        return JsonResponse({'highest_bid': int(get_highest_bid(id))})

    return render(request, 'products/product_details.html', {
        'product': get_object_or_404(Product, pk=id), 'highest_bid': int(get_highest_bid(id))
    })


def place_bid(productid, bidder, amount):
    product_prev_bids = ProductOffer.objects.filter(product_id=productid)
    user_prev_bid = product_prev_bids.filter(bidder_id=bidder)

    prev_bid = [{
        'id': x.id,
        'product': x.product_id,
        'bidder': x.bidder_id,
        'amount': x.offer_amount
    } for x in user_prev_bid]

    if prev_bid:
        if amount > prev_bid[0]['amount']:
            user_prev_bid.update(offer_amount=amount)
            return {'status': 'bid_updated', 'bid_amount': int(amount), 'message': 'You have increased your bid to: ' +
                    str(int(amount)) + ' ISK',
                    'product': prev_bid[0]['product']}
        else:
            return {'status': 'bid_unsuccessful', 'bid_amount': int(prev_bid[0]['amount']),
                    'message': 'Must be greater than your current bid: ' +
                    str(int(prev_bid[0]['amount'])) + ' ISK',
                    'product': prev_bid[0]['product']}
    else:
        bid_created = create_bid(productid, bidder, amount)
        if bid_created:
            return {'status': 'bid_success', 'bid_amount': int(amount), 'message': 'You have placed a new bid of: ' +
                    str(int(amount)) + ' ISK',
                    'product': productid}
        else:
            return {'status': 'bid_unsuccessful', 'bid_amount': int(amount),
                    'message': 'Unable to place your bid for: ' + str(int(amount)) + ' ISK',
                    'product': productid}


def create_bid(productid, bidder, amount):
    product_offer = ProductOffer()
    product_offer.product_id = productid
    product_offer.bidder = bidder
    product_offer.offer_amount = amount
    product_offer.save()
    return product_offer


def get_highest_bid(id):
    product_bids = ProductOffer.objects.filter(product_id=id)
    order_bids = product_bids.order_by('-offer_amount')
    sorted_bids = [{
        'id': x.id,
        'product': x.product_id,
        'bidder': x.bidder_id,
        'amount': int(x.offer_amount)
    } for x in order_bids]

    if sorted_bids:
        return sorted_bids[0]['amount']
    else:
        amount = 0
        return amount


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