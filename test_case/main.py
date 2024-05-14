import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import page

# only the methods/ tests with the "test" in the beginning will run and others wont

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        print("setup") # the setup method is called for everytime a test case in run, if two test cases are run then the setup is run two times
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.python.org")
    def test_title(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_matches()

    def test_example2(self):
        assert True

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()