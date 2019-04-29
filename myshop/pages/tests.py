from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from pages.views import index, contact, product_list, register


class TestUrls(SimpleTestCase):
    
    def test_home_url_is_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)

    def test_contact_url_is_resolves(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)

    def test_product_list_url_is_resolves(self):
        url = reverse('shop')
        self.assertEquals(resolve(url).func, product_list)