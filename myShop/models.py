from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название товара')
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, verbose_name='Категория товара')
    created_at = models.DateField(auto_now_add=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество на складе')
    image = models.ImageField(upload_to='myShop/', verbose_name='Картинка товара')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена товара')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class SerialNumber(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=100, verbose_name='Серийный номер товара')

    def __str__(self):
        return f'{self.product}-{self.serial_number}'

class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField(default='хороший товар')
    mark = models.PositiveBigIntegerField(default=5, validators=[MinValueValidator(1),MaxValueValidator(5)])
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.product}-{self.mark}'    