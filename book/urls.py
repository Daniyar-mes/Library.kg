from django.urls import path
from book.views import about_me, my_favorite_writers, sayings_of_great_poets

urlpatterns = [
    path('about/', about_me, name='about'),
    path('favorite/', my_favorite_writers, name='favorite'),
    path('poets/', sayings_of_great_poets, name='poets')
]