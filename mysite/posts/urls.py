from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    # ex: /posts/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /posts/5/
    path('<int:pk>/', views.PostPage.as_view(), name='post_page'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
]