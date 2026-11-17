from django.urls import path
from orders.views import (
    OrderListView, 
    CreateOrderView, 
    UpdateOrderView, 
    DeleteOrderView)


urlpatterns = [
    path('create_order/', CreateOrderView.as_view(), name='create_order'),
    path('order_list/', OrderListView.as_view(), name='order_list'),
    path('order_list/<int:id>/edit/', UpdateOrderView.as_view(), name='update_order'),
    path('order_list/<int:id>/drop/', DeleteOrderView.as_view(), name='drop_order'),
]