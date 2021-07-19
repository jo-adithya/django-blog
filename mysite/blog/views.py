from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment,
from .forms import PostForm, CommentForm

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_at__lte=timezone.now().order_by('-published_at'))


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post
    fields = ('author', 'title', 'body')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post
    fields = ('author', 'title', 'body')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    model = Post
    context_object_name = 'deleted_post'
    success_url = reverse_lazy('blog:post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published_at__isnull=True).order_by('-created_at')
