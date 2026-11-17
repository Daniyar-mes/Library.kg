from django.contrib import admin
from CineBoard.models import Genre, Movie, Comment, VIPBooking

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(VIPBooking)
admin.site.register(Comment)