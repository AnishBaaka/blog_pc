from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from App.models import Post
# Create your views here.

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'author']
    template_name = "post_form.html"
    success_url = reverse_lazy('home')

class PostList(ListView):
    model = Post
    template_name = 'index.html'

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content', 'author']
    template_name = "post_form.html"
    success_url = reverse_lazy('home')