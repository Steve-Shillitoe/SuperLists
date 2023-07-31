"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

# TODO: Configure your database in settings.py and sync before running tests.

class HomePageTest(TestCase):

    def test_home(self):
        """Tests the home page."""
        #response = self.client.get('/')
        #self.assertContains(response, 'Home Page', 1, 200)
        found = resolve('/')
        self.assertEqual(found.func, home_page)

   