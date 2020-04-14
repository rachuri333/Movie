from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from movieapp.models import movie
from django.urls import reverse_lazy
#
class MovieListView(ListView):
    model=movie
    template_name='movieapp/movies.html'
    context_object_name='movie_list'
class MovieDetailView(DetailView):
    model=movie

class MovieCreateView(CreateView):
    model=movie
    fields=('MovieName','Timing','Location')

class MovieUpdateView(UpdateView):
    model=movie
    fields=('MovieName','Timing','Location')

class MovieDeleteView(DeleteView):
    model=movie
    template_name='movieapp/movie_confirm_delete.html'
    success_url=reverse_lazy('list')
