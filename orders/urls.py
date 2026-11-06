from django.urls import path
from orders.views import (
    order_list_view, 
    create_order_view, 
    update_order_view, 
    delete_order_view)


urlpatterns = [
    path('create_order/', create_order_view, name='create_order'),
    path('order_list/', order_list_view, name='order_list'),
    path('order_list/<int:id>/edit/', update_order_view, name='update_order'),
    path('order_list/<int:id>/drop/', delete_order_view, name='drop_order'),
]