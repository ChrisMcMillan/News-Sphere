from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('posts:index')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = RichTextField(blank=True, null=True, max_length=5000)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='uploads/profile')
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('posts:index')

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=50)
    post_image = models.ImageField(null=True, blank=True, upload_to='uploads/images')
    post_description = RichTextField(blank=True, null=True, max_length=5000)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    votes = models.ManyToManyField(User, related_name='news_posts')

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('posts:index')

    def total_votes(self):
        return self.votes.count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=280)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text
