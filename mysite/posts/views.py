
from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import Post, Category, Comment
from .forms import PostForm, AddCommentForm
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_posts_list'

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['cat_menu'] = cat_menu
        return context

    def get_queryset(self):
        """Return the last ten published posts."""
        return Post.objects.order_by('-pub_date')[:10]

class PostPage(generic.DetailView):
    model = Post
    template_name = 'posts/post_page.html'

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['cat_menu'] = cat_menu

        data = get_object_or_404(Post, id=self.kwargs['pk'])
        total_votes = data.total_votes()
        context['total_votes'] = total_votes

        upvoted = False
        if data.votes.filter(id=self.request.user.id).exists():
            upvoted = True
        context['upvoted'] = upvoted

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

class AddCommentView(generic.CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'posts/add_comment.html'
    success_url = reverse_lazy('posts:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

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

def VoteView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    if post.votes.filter(id=request.user.id).exists():
        post.votes.remove(request.user)

    else:
        post.votes.add(request.user)

    return HttpResponseRedirect(reverse('posts:post_page', args=[str(pk)]))

def CategoryPage(request, cats):

    newCats = cats.replace('-', ' ')
    category_posts = Post.objects.filter(category__name__contains=newCats)
    return render(request, 'posts/categories.html', {'cats':newCats.title(), 'category_posts':category_posts})
