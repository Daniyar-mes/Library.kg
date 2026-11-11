from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='укажите название книги')
    author = models.CharField(max_length=100, verbose_name='укажите автора')
    genre = models.CharField(max_length=50, verbose_name='укажите жанр')
    publication_year = models.PositiveIntegerField(verbose_name='укажите год публикации')
    pages = models.PositiveIntegerField(verbose_name='укажите количество страниц')
    publisher = models.CharField(max_length=100, verbose_name='укажите издательство')
    image = models.ImageField(upload_to='book/', verbose_name='загрузите картинку')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='укажите цену')


    GENRE_BOOK = (
        ('Фантастика','Фантастика'),
        ('Фэнтези', 'Фэнтези'),
        ('Детектив', 'Детектив'),
        ('Роман', 'Роман'),
        ('Приключения', 'Приключения'),
        ('Ужасы', 'Ужасы'),
        ('Историческая литература', 'Историческая литература'),
        ('Научно-популярная литература', 'Научно-популярная литература')
    )

    genre_book = models.CharField(max_length=200, choices=GENRE_BOOK, verbose_name='жанры книг')
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0, null=True)
    

    class Meta:
        verbose_name = 'книги'
        verbose_name_plural = 'книга'

    def __str__(self):
        return self.title









