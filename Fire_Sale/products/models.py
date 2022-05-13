from django.db import models
#from user.models import Profile
from django.contrib.auth.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    #image = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    #highest_offer = models.ForeignKey()
    #similar_items = models.ForeignKey()
    #place_order_button

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    #price = models.FloatField()
    on_sale = models.BooleanField() #Er seljandi búinn að accepta annað tilboð

    #Impossible to add a non-nullable field 'seller' to product without specifying a default.
    seller = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.CharField(max_length=9999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class ProductOffer(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    offer_amount = models.FloatField()

class OrderInformation(models.Model):
    #buyerID?
    #sellerID?
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    cardholder = models.CharField(max_length=100)
    cardnumber = models.CharField(max_length=19)
    exp = models.CharField(max_length=5)
    cvc = models.CharField(max_length=3)
