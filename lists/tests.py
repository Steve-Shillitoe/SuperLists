"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest
from lists.models import Item

# TODO: Configure your database in settings.py and sync before running tests.

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_send_a_post_request(self):
        response = self.client.post('/', data={'item_text':'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'lists/home.html')

 
class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'The second (ever) list item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual('The first (ever) list item', first_saved_item.text)
        self.assertEqual('The second (ever) list item', second_saved_item.text)