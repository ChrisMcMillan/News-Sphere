
from django.views import generic
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.shortcuts import render

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_posts_list'

    def get_queryset(self):
        """Return the last five published posts."""
        return Post.objects.order_by('-pub_date')[:5]

class PostPage(generic.DetailView):
    model = Post
    template_name = 'posts/post_page.html'

class AddPost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/add_post.html'
    # fields = '__all__'
    # fields = ('user', 'post_title', 'post_image', 'post_description')

class EditPost(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/update_post.html'
    # fields = ('post_title', 'post_image', 'post_description')

class DeletePost(generic.DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('posts:index')

def CategoryPage(request, cats):

    category_posts = Post.objects.filter(category__name__contains=cats)
    return render(request, 'posts/categories.html', {'cats':cats, 'category_posts':category_posts})
