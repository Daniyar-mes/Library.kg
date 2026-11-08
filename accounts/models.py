from django.db import models

class CustomUser(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Мужской'),
        ('Female', 'Женский'),
    ]

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255) # Хранить будем хэш
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars/')
    phone_number = models.CharField(max_length=20, default='996')
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    city = models.CharField(max_length=25, default='Bishkek')

    def __str__(self):
        return self.email
