import time
import unittest2
from selenium import webdriver


class setUpClassAndtearDownClass(unittest2.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()
