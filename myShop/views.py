from django.shortcuts import render, get_object_or_404
from myShop.models import Product

def myShop_list_view(request):
    if request.method == "GET":
        products = Product.objects.all().order_by('-id')
    return render(request, 'myShop_list.html', {'products': products})

def product_detail_view(request, id):
    product_id = get_object_or_404(Product, id=id)
    return render(request, 'myShop_detail.html', {'product': product_id})
