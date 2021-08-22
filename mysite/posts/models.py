from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=50)
    post_image = models.ImageField(null=True, blank=True, upload_to='uploads/images')
    post_description = models.TextField(max_length=280)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        # return reverse('post_page', args=(str(self.id)))
        return reverse('posts:index')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=280)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text
