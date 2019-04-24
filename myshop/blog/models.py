from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

"""
Below is 
"""
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()\
                          .filter(status='published')

"""
Below is the post model which has choices enabling me to choose if a post
is a draft to save for later or to be published.
This also has get absolute url for humanized and seo friendly urls.
The foreignkey will define a many to one relationship.

"""
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField(blank=True)
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.published.year,
                             self.published.month,
                             self.published.day,
                             self.slug])

    class Meta:
        ordering = ('published',)

    def __str__(self):
        return self.title