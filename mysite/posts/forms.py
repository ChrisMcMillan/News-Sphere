from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('user', 'post_title', 'post_image', 'post_description')
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'post_title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'post_image': forms.ImageField(attrs={'class': 'form-control'}),
            'post_description': forms.Textarea(attrs={'class': 'form-control'}),
        }

