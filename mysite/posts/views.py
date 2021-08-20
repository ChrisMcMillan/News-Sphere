from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Post

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_posts_list'

    def get_queryset(self):
        """Return the last five published posts."""
        return Post.objects.order_by('-pub_date')[:5]

class PostPage(generic.DetailView):
    model = Post
    template_name = 'posts/post_page.html'

