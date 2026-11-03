from django.contrib import admin
from myShop.models import Product, SerialNumber, ProductComment

admin.site.register(Product)
admin.site.register(SerialNumber)
admin.site.register(ProductComment)
