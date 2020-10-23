from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #Author connected to actual authenticated default user
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment = True) #approved comment defined in Comment model

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk' :self.pk})

    def __str__(self):
        return self.title 

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name= 'comments', on_delete=models.CASCADE) #connecting to post and related name
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post_list', kwargs= {'pk' :self.pk})
