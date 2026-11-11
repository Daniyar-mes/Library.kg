from django.urls import path
from book.views import about_me, my_favorite_writers, sayings_of_great_poets, book_list_view, book_detail_view, book_search_view

urlpatterns = [
    path('about/', about_me, name='about'),
    path('favorite/', my_favorite_writers, name='favorite'),
    path('poets/', sayings_of_great_poets, name='poets'),
    path('book_list/', book_list_view, name='book_list'),
    path('book_list/<int:id>/', book_detail_view, name='book_detail'),
    path('search/', book_search_view, name='search'),
]