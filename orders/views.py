from django.shortcuts import render, redirect, get_object_or_404
from orders.forms import OrdersForm
from orders.models import Orders
from django.views import generic


# CREATE
class CreateOrderView(generic.CreateView):
    template_name = 'orders_create.html'
    form_class = OrdersForm
    success_url = '/order_list/'

    def form_valid(self, form):
        return super(CreateOrderView, self).form_valid(form=form)

# def create_order_view(request):
#     if request.method == "POST":
#         form_order = OrdersForm(request.POST, request.FILES)
#         if form_order.is_valid():
#             form_order.save()
#             return redirect('order_list')
#     else:
#         form_order = OrdersForm()

#     return render(request, 'orders_create.html', {'form': form_order})


# READ
class OrderListView(generic.ListView):
    template_name = 'order_list.html'
    context_object_name = 'order'
    model = Orders
    ordering = ('-id')

    def get_queryset(self):
        return self.model.objects.all().order_by(self.ordering)   

# def order_list_view(request):
#     order_list = Orders.objects.all().order_by('-id')
#     return render(request, 'order_list.html', {'order': order_list})


# UPDATE
class UpdateOrderView(generic.UpdateView):
    template_name = 'order_update.html'
    model = Orders
    form_class = OrdersForm
    success_url = '/order_list/'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=order_id)

    def form_valid(self, form):
        return super(UpdateOrderView, self).form_valid(form=form)
    
# def update_order_view(request, id):
#     order_id = get_object_or_404(Orders, id=id)

#     if request.method == "POST":
#         form_order = OrdersForm(request.POST, request.FILES, instance=order_id)

#         if form_order.is_valid():
#             form_order.save()
#             return redirect('order_list')
#     else:
#         form_order = OrdersForm(instance=order_id)
#     return render(request, 'order_update.html', {'form': form_order})


# DELETE
class DeleteOrderView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    context_object_name = 'order_id'
    success_url = '/order_list/'
    model = Orders

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=order_id)

# def delete_order_view(request, id):
#     order_id = get_object_or_404(Orders, id=id)

#     if request.method == "POST":
#         order_id.delete()
#         return redirect('order_list')