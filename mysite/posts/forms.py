from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('user', 'category', 'post_title', 'post_image', 'post_description')
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'author_input', 'type':'hidden'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'post_title': forms.TextInput(attrs={'class': 'form-control'}),
            'post_description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)
        widgets = {
            'comment_text': forms.Textarea(attrs={'class': 'form-control'}),
        }
