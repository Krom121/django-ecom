from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from blog.views import PostListView, post_detail
from blog.models import Post
from django.utils import timezone


class TestUrls(SimpleTestCase):

    def test_post_list_url_is_resolves(self):
        url = reverse('blog:post_list')
        self.assertEquals(resolve(url).func.view_class, PostListView)
