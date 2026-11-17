from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='укажите название фильма')
    description = models.TextField(verbose_name='введите краткое описание фильма')
    release_year = models.PositiveIntegerField(verbose_name='укажите год выпуска')
    director = models.CharField(max_length=100, verbose_name='укажите режиссера')
    country = models.CharField(max_length=100, verbose_name='страна')
    duration = models.PositiveIntegerField(verbose_name='продолжительность')
    poster = models.ImageField(upload_to='movies/', verbose_name='загрузите картинку')
    genres = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    description = models.TextField(default='[хороший фильм]')
    mark = models.PositiveBigIntegerField(default=5, validators=[MinValueValidator(1),MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.movie}-{self.mark}'


class VIPBooking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=200, verbose_name='укажите место')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie}-{self.user}'
    
    