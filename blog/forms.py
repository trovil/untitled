__author__ = 'Kompik'
from django import forms

from .models import Post,Comment,Tag

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','image','video', 'text','tags')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ('tag',)