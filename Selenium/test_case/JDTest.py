import os
import sys


CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))
if PKG_DIR not in sys.path:
    sys.path.append(PKG_DIR)

from selenium.webdriver.support.select import Select
import unittest2
import time
from selenium.webdriver import ActionChains
from test_case.BaseTestCase import setUpClassAndtearDownClass


class JDTest(setUpClassAndtearDownClass):
    def setUp(self):
        self.driver.get('https://www.jd.com/')
        self.driver.find_element_by_link_text("你好，请登录").click()
        self.driver.find_element_by_link_text("账户登录").click()
        self.driver.find_element_by_id("loginname").clear()
        self.driver.find_element_by_id("loginname").send_keys('loginname')
        self.driver.find_element_by_id("nloginpwd").clear()
        self.driver.find_element_by_id("nloginpwd").send_keys('password')
        self.driver.find_element_by_id("loginsubmit").click()
        # 手工滑动验证框
        time.sleep(15)

    def tearDown(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_class_name("nickname")).perform()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_class_name("link-logout")).click().perform()

    def test_2Shopping(self):
        self.driver.find_element_by_id("key").clear()
        self.driver.find_element_by_id("key").send_keys("索尼电视")
        self.driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[2]/div/div[2]/button/i").click()
        self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[3]/div/div[7]/a[3]").click()

    def test_1home(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/ul[3]/li[1]/div[1]/a").click()
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/a").click()
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
        self.driver.find_element_by_css_selector("[value='0']").click()
        birthdayYear = self.driver.find_element_by_id("birthdayYear")
        Select(birthdayYear).select_by_visible_text("1990")
        birthdayMonth = self.driver.find_element_by_id("birthdayMonth")
        Select(birthdayMonth).select_by_visible_text("1")
        birthdayDay = self.driver.find_element_by_id("birthdayDay")
        Select(birthdayDay).select_by_visible_text("1")
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div[2]/div[1]/div/div[6]/div/ul/li[1]/div").click()
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div[2]/div[1]/div/div[6]/div/ul/li[2]/div").click()
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div[2]/div[1]/div/div[6]/div/ul/li[3]/div").click()
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div[2]/div[1]/div/div[6]/div/ul/li[4]/div").click()
        self.driver.find_element_by_link_text("提交").click()


if __name__ == '__main__':
    unittest2.main()