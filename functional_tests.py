
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

        
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')

        inputbox.send_keys('Buy ferret food')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('2: Feed ferrets')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #Generator expression that generates values on-the-fly as you iterate through them
        #Similiar to a list comprehension but uses () not []
        self.check_for_row_in_list_table('1: Buy ferret food')
        self.check_for_row_in_list_table('2: Feed ferrets')

        self.fail('Finish the test!')



unittest.main(warnings='ignore')

