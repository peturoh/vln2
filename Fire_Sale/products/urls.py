from django.urls import path
from . import views
from products.forms import CheckoutForm1, CheckoutForm2, CheckoutForm3
from products.views import CheckoutWizard

urlpatterns = [
    path('', views.index, name='product-index'),
    path('<int:id>', views.get_product_by_id, name="product-details"),
    path('checkout/', CheckoutWizard.as_view([CheckoutForm1, CheckoutForm2, CheckoutForm3]), name="checkout"),
    path('create_product/', views.create, name="create_product"),
    path('my_listings/', views.get_my_listings, name="my_listings")
]
