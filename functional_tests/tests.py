
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from django.test import LiveServerTestCase
import time
import unittest

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()


    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError, WebDriverException) as e:
                if time.time - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

        
    def test_can_start_a_list_for_one_user(self):
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')

        #User enters a to-do item
        inputbox.send_keys('Buy ferret food')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy ferret food')

        #user enters a second to-do item
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Feed ferrets')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('2: Feed ferrets')

    
    def test_multiple_users_can_start_lists_at_different_urls(self):
        #user starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy ferret food')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy ferret food')
        
        #user notices that their list has a unique URL
        first_user_list_url = self.browser.current_url
        self.assertRegex(first_user_list_url, '/lists/.+')

        # A second user comes to the website
        ## We use a new browser session to ensure no information is
        ## coming through from the first user
        self.browser.quit()
        self.browser = webdriver.Chrome()

        #Second user visits the home page. There is no sign of the first user's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy ferret food', page_text)
        self.assertNotIn('Feed ferrets', page_text)

        #Second user starts a new list
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy cat food')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy cat food')

        #Second user gets their own unique url
        second_user_list_url = self.browser.current_url
        self.assertRegex(second_user_list_url, '/lists/.+')
        self.assertNotEqual(second_user_list_url, first_user_list_url)

        #Check there is still no trace of first user's list
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy ferret food', page_text)
        self.assertIn('Buy cat food', page_text)

