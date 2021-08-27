from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    # ex: /posts/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /posts/5/
    path('<int:pk>/', views.PostPage.as_view(), name='post_page'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('edit_post/<int:pk>', views.EditPost.as_view(), name='edit_post'),
    path('delete_post/<int:pk>', views.DeletePost.as_view(), name='delete_post'),
]