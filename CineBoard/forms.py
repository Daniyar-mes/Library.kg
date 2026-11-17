from django import forms
from .models import Movie, Comment, VIPBooking


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_year', 'director', 'country', 'duration', 'poster', 'genres']
        widgets = {
            'genres': forms.CheckboxSelectMultiple(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description', 'mark']
        labels = {
            'description': 'Ваш отзыв',
            'mark': 'Оценка (от 1 до 5)',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'mark': forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'form-control'}),
        }


class VIPBookingForm(forms.ModelForm):
    class Meta:
        model = VIPBooking
        fields = ['movie', 'seat_number']
        labels = {
            'movie': 'Выберите фильм',
        }
