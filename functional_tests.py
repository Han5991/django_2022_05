from selenium import webdriver
import unittest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def set_chrome_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())


class FunctionalTest(unittest.TestCase):

    def setUp(self):
        self.browser = set_chrome_driver()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_start(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!!!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
