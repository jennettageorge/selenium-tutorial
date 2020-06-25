import unittest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class WebCode(unittest.TestCase):

    def setUp(self):
        opts = Options()
        opts.headless = True

        self.driver = webdriver.Firefox(options=opts)

    def test_title(self):

        self.driver.get('http://webcode.me')
        self.assertIn("My html page", self.driver.title)


    def test_paragraphs(self):

        self.driver.get('http://webcode.me')

        els = self.driver.find_elements_by_tag_name('p')

        self.assertIn('Today is a beautiful day', els[0].text)
        self.assertIn('Hello there', els[1].text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
