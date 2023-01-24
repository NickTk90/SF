from .models import Post

from django.views.generic import ListView, DetailView

from django.shortcuts import render

class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-dateCreation'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'posts.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'


class ShowPost(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'




def index(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', context={'posts':posts})

