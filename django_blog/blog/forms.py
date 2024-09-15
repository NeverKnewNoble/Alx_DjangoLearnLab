from django import forms
from taggit.forms import TagField  # Import TagField for handling tags
from .models import Post, Comment

class PostForm(forms.ModelForm):
    tags = TagField(required=False)  # Use TagField for tag input

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include 'tags' in fields

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
