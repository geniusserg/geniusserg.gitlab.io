import unittest
from Selenium import webdriver
import time

class TestBrowserOpen(unittest.TestCase):
    def test_a(self):
        driver = webdriver.Remote()
        driver.maximize_window()
        driver.get("https://localhost:8080")
        title = driver.title()
        print(title)
        if (title == "WebCarConfig"):
            assert BaseException
        time.sleep(3)
        driver.close()
