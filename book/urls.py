from django.urls import path
from book.views import AboutMeView, MyFavoriteWritersView, SayingsGreatPoetsView, BookListView, BookDetailView, BookSearchView

urlpatterns = [
    path('about/', AboutMeView.as_view(), name='about'),
    path('favorite/', MyFavoriteWritersView.as_view(), name='favorite'),
    path('poets/', SayingsGreatPoetsView.as_view(), name='poets'),
    path('book_list/', BookListView.as_view(), name='book_list'),
    path('book_list/<int:id>/', BookDetailView.as_view(), name='book_detail'),
    path('search/', BookSearchView.as_view(), name='search'),
]