from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from .models import Movie, Genre, Comment, VIPBooking
from .forms import MovieForm, CommentForm, VIPBookingForm


class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movies'
    ordering = ['-id']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        genre_id = self.request.GET.get('genre')
        if genre_id:
            queryset = queryset.filter(genres__id=genre_id)
        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        return context


class MovieDetailView(FormMixin, DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'
    pk_url_kwarg = 'id'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('movie_detail', kwargs={'id': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comment_set.all().order_by('-created_at')
        if 'form' not in context:
            context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.movie = self.object
        comment.user = self.request.user
        comment.save()
        return super().form_valid(form)


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie')


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('movie')


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'movie_confirm_delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('movie')


class VIPBookingCreateView(LoginRequiredMixin, CreateView):
    model = VIPBooking
    form_class = VIPBookingForm
    template_name = 'vip_booking.html'
    success_url = reverse_lazy('vip_status')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, 'vipbooking'):
            return redirect('vip_status')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        vip = form.save(commit=False)
        vip.user = self.request.user
        vip.save()
        return super().form_valid(form)


class VIPStatusView(LoginRequiredMixin, DetailView):
    model = VIPBooking
    template_name = 'vip_status.html'
    context_object_name = 'vip'

    def get_object(self, queryset=None):
        return get_object_or_404(VIPBooking, user=self.request.user)
