
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

class AddPost(generic.CreateView):
    model = Post
    template_name = 'posts/add_post.html'
    # fields = '__all__'
    fields = ('user', 'post_title', 'post_image', 'post_description')
