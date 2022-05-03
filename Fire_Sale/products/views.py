from django.shortcuts import render

products = [
    {'name': 'BMX Hjól', 'price': 25000},
    {'name': '66n Húfa', 'price': 5900}
]

# Create your views here.
def index(request):
    return render(request, 'products/index.html', context={'products': products})
