from django.urls import path
from CineBoard.views import (
    MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView, MovieDeleteView,
    VIPBookingCreateView, VIPStatusView
)

urlpatterns = [
    path('movie/', MovieListView.as_view(), name='movie'),
    path('movie/<int:id>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/add/', MovieCreateView.as_view(), name='movie_add'),
    path('movie/<int:id>/edit/', MovieUpdateView.as_view(), name='movie_edit'),
    path('movie/<int:id>/delete/', MovieDeleteView.as_view(), name='movie_delete'),

    path('vip/book/', VIPBookingCreateView.as_view(), name='vip_book'),
    path('vip/my/', VIPStatusView.as_view(), name='vip_status'),
]

