from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product-index'),
    path('<int:id>', views.get_product_by_id, name="product-details")
]
