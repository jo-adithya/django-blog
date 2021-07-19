from django import forms
from django.forms import widgets
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'body')
    
        widgets = {
            'author': forms.TextInput(attrs={'class': 'post-title'}),
            'title': forms.TextInput(attrs={'class': 'post-title'}),
            'body': forms.Textarea(attrs={'class': 'editable medium-editor-textarea post-body'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'comment')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'post-title'}),
            'comment': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
