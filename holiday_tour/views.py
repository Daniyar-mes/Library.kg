from django.shortcuts import render
from holiday_tour.models import Tour, Booking

def holiday_tour_list_view(request):
    if request.method == "GET":
        tour = Tour.objects.all().order_by('-id')
        booking = Booking.objects.select_related(
            'person', 'tour_booking'
        ).all()

    return render(request, 'holiday_tour_list.html', {
        'tour': tour,
        'booking': booking
    })
