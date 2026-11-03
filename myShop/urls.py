from django.urls import path
from myShop.views import myShop_list_view, product_detail_view


urlpatterns = [
    path('myShop/', myShop_list_view, name='myShop'),
    path('myShop/<int:id>/', product_detail_view, name='myShop_detail'),
]