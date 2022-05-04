from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    #highest_offer = models.ForeignKey()
    #similar_items = models.ForeignKey()
    #place_order_button

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    #price = models.FloatField()
    on_sale = models.BooleanField() #Er seljandi búinn að accepta annað tilboð
    #manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

class ProductImage(models.Model):
    image = models.CharField(max_length=9999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)