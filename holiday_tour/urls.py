from django.urls import path
from holiday_tour.views import holiday_tour_list_view


urlpatterns = [
    path('holiday_tour/', holiday_tour_list_view, name='holidaytour'),
]