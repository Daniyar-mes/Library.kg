from django.shortcuts import render, redirect, get_object_or_404
from orders.forms import OrdersForm
from orders.models import Orders

# CREATE
def create_order_view(request):
    if request.method == "POST":
        form_order = OrdersForm(request.POST, request.FILES)
        if form_order.is_valid():
            form_order.save()
            return redirect('order_list')
    else:
        form_order = OrdersForm()

    return render(request, 'orders_create.html', {'form': form_order})


# READ
def order_list_view(request):
    order_list = Orders.objects.all().order_by('-id')
    return render(request, 'order_list.html', {'order': order_list})


# UPDATE
def update_order_view(request, id):
    order_id = get_object_or_404(Orders, id=id)

    if request.method == "POST":
        form_order = OrdersForm(request.POST, request.FILES, instance=order_id)

        if form_order.is_valid():
            form_order.save()
            return redirect('order_list')
    else:
        form_order = OrdersForm(instance=order_id)

    return render(request, 'order_update.html', {'form': form_order})


# DELETE
def delete_order_view(request, id):
    order_id = get_object_or_404(Orders, id=id)

    if request.method == "POST":
        order_id.delete()
        return redirect('order_list')