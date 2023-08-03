"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest

# TODO: Configure your database in settings.py and sync before running tests.

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_send_a_post_request(self):
        response = self.client.post('/', data={'item_text':'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'lists/home.html')

   