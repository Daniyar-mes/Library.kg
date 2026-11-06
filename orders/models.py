from django.db import models

class Orders(models.Model):

    STATUS_CHOICES = (
    ('NEW', 'Новый'),
    ('PROCESSING', 'В обработке'),
    ('DELIVERED', 'Доставлен'),
)
    order_number = models.CharField(max_length=200, verbose_name='Номер заказа')
    customer_name = models.CharField(max_length=200, verbose_name='Ф.И.О заказчика')
    product_name = models.CharField(max_length=100, verbose_name='Название товара')
    quantity = models.PositiveIntegerField(verbose_name='Количество товара')
    image = models.ImageField(upload_to='orders/', verbose_name='Картинка товара')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена заказа')
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, verbose_name='Статус заказа')
    created_at = models.DateField(auto_now_add=True)

