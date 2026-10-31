from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

class Category(models.Model):
    category_tour = models.CharField(max_length=100)

    def __str__(self):
        return self.category_tour
    

class Tour(models.Model):
    title = models.CharField(max_length=100, default='Жемчужина Кыргызстана')
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    booking_date = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title
    

class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Booking(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    tour_booking = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.person}-{self.tour_booking}'   


class Comment(models.Model):
    choice_tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    description = models.TextField(default='[хороший тур]')
    mark = models.PositiveBigIntegerField(default=5, validators=[MinValueValidator(1),MaxValueValidator(5)])
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.choice_tour}-{self.mark}'