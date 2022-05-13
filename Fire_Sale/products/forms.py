from django import forms
from django.forms import ModelForm, widgets
from products.models import Product


class CheckoutForm1(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    address2 = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    zip = forms.CharField(max_length=100)

class CheckoutForm2(forms.Form):
    cardholder = forms.CharField(max_length=100)
    cardnumber = forms.CharField(max_length=19)
    exp = forms.CharField(max_length=5)
    cvc = forms.CharField(max_length=3)

class CheckoutForm3(forms.Form):
    accept = forms.BooleanField()

class CreateItemForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    class Meta:
        model = Product
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'on_sale': widgets.CheckboxInput(attrs={'class': 'form-control'})
        }

