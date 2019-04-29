from django.test import TestCase, Client
from django.urls import reverse
from shop.models import Product, Category


class TestViews(TestCase):

    def test_product_list_GET(self):
        client = Client()
        response = client.get(reverse('shop:product_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')