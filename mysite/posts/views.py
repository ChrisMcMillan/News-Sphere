
from django.views import generic
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import PostForm
from django.shortcuts import render

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_posts_list'

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['cat_menu'] = cat_menu
        return context

    def get_queryset(self):
        """Return the last five published posts."""
        return Post.objects.order_by('-pub_date')[:5]

class PostPage(generic.DetailView):
    model = Post
    template_name = 'posts/post_page.html'

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['cat_menu'] = cat_menu
        return context

class AddPost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/add_post.html'

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['cat_menu'] = cat_menu
        return context

class EditPost(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/update_post.html'

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['cat_menu'] = cat_menu
        return context

class DeletePost(generic.DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('posts:index')

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['cat_menu'] = cat_menu
        return context

def CategoryPage(request, cats):

    newCats = cats.replace('-', ' ')
    category_posts = Post.objects.filter(category__name__contains=newCats)
    return render(request, 'posts/categories.html', {'cats':newCats.title(), 'category_posts':category_posts})
