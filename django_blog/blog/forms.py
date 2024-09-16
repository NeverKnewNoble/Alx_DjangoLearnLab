# blog/forms.py
from django import forms
from taggit.forms import TagWidget  # Import TagWidget for tag input
from .models import Post, Comment

class PostForm(forms.ModelForm):
    tags = forms.CharField(widgets=TagWidget(), required=False)  # Use TagWidget for tag input

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include 'tags' in fields

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
