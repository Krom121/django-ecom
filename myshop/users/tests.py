from django.test import TestCase, SimpleTestCase
from users.forms import UserRegisterForm

class TestForms(SimpleTestCase):

    def test_register_form_valid_data(self):
        form = UserRegisterForm(data={
            'username': 'stephen',
            'email': 'stephen@gmail.com'

        })

        self.assertTrue(form.is_valid())

    def test_register_form_no_data(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())

        self.assertEquals(len(form.errors), 3)