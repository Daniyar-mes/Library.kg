from django.contrib import admin
from holiday_tour.models import Category, Tour, Person, Booking, Comment

admin.site.register(Category)
admin.site.register(Tour)
admin.site.register(Person)
admin.site.register(Booking)
admin.site.register(Comment)