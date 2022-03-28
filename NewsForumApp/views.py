from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from datetime import datetime
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'Posts.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'
    ordering = ['-postTime']
    paginate_by = 10
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        return context


class PostDetails(DetailView):
    model = Post
    template_name = 'Post.html'


class PostListSearch(ListView):
    model = Post
    template_name = 'Post_search.html'
    context_object_name = 'posts'
    ordering = ['-postTime']
    paginate_by = 1
    form_class = PostForm

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args,
                         **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter()
        }


class PostCreateView(CreateView):
    template_name = 'Post_create.html'
    form_class = PostForm
    success_url = '/news/'


class PostUpdateView(UpdateView):
    template_name = 'Post_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
    success_url = '/news/'


class PostDeleteView(DeleteView):
    template_name = 'Post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

