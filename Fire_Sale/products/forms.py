from django import forms

class CheckoutForm1(forms.Form):
    username = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    address2 = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    zip = forms.CharField(max_length=100)

class CheckoutForm2(forms.Form):
    cardholder = forms.CharField(max_length=100)
    cardnumber = forms.CharField(max_length=19)
    exp = forms.CharField(max_length=4)
    cvc = forms.CharField(max_length=3)