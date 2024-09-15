# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django_taggit.models import Tag
from .models import Post, Comment
from .forms import PostForm, CommentForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            return super().post(request, *args, **kwargs)
        return redirect('post_list')

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            return super().post(request, *args, **kwargs)
        return redirect('post_list')

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            return super().post(request, *args, **kwargs)
        return redirect('post_list')

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            return super().post(request, *args, **kwargs)
        return redirect('post_detail', pk=self.kwargs['post_id'])

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            return super().post(request, *args, **kwargs)
        return redirect('post_detail', pk=self.object.post.pk)

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            return super().post(request, *args, **kwargs)
        return redirect('post_detail', pk=self.object.post.pk)

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        return Post.objects.filter(tags__slug=tag_slug)

class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
        )

class UserRegisterView(FormView):
    template_name = 'blog/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class UserLoginView(FormView):
    template_name = 'blog/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'blog/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user
