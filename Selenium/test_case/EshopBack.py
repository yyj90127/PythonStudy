import os
import sys

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))
if PKG_DIR not in sys.path:
    sys.path.append(PKG_DIR)

import time
import unittest2
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from test_case.BaseTestCase import setUpClassAndtearDownClass
from test_tools.csvFilesManager import readcsv
import ddt


@ddt.ddt
class Eship(setUpClassAndtearDownClass):
    def setUp(self):
        self.driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        # 后台登录
        self.driver.find_element_by_name("username").clear()
        self.driver.find_element_by_name("username").send_keys("admin")
        self.driver.find_element_by_name("userpass").clear()
        self.driver.find_element_by_name("userpass").send_keys("password")
        self.driver.find_element_by_name("userverify").clear()
        self.driver.find_element_by_name("userverify").send_keys("1234")
        self.driver.find_element_by_class_name("Btn").click()

    def tearDown(self):
        # 登出
        self.driver.switch_to.default_content()
        self.driver.find_element_by_link_text("退出系统").click()

    def test_ManageProduct(self):
        # 商品管理
        self.driver.find_element_by_link_text("商品管理").click()
        self.driver.find_element_by_link_text("添加商品").click()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_name("name").send_keys("iphone12 pro max")
        self.driver.find_element_by_id("1").click()
        self.driver.find_element_by_id("2").click()
        self.driver.find_element_by_id("6").click()
        ActionChains(self.driver).double_click(self.driver.find_element_by_id("7")).perform()
        brand = self.driver.find_element_by_class_name("select")
        Select(brand).select_by_value("1")
        self.driver.find_element_by_name("is_hot").click()
        self.driver.find_element_by_link_text("商品规格").click()
        self.driver.find_element_by_name("_shop_price[0]").clear()
        self.driver.find_element_by_name("_shop_price[0]").send_keys("10099.00")
        self.driver.find_element_by_name("_market_price[0]").clear()
        self.driver.find_element_by_name("_market_price[0]").send_keys("10899.00")
        self.driver.find_element_by_name("_cost_price[0]").clear()
        self.driver.find_element_by_name("_cost_price[0]").send_keys("8999.00")
        self.driver.find_element_by_link_text("商品图册").click()
        # driver.find_element_by_css_selector("#uploader .placeholder label[style]").click()
        self.driver.find_element_by_name("file").send_keys("C:/Users/yuanyijun/Desktop/epolicy.jpg")
        self.driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()
        WebDriverWait(self.driver,30,0.5).until(expected_conditions.alert_is_present())
        result = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        if result == "上传成功":
            self.driver.find_element_by_class_name("button_search").click()
        else:
            print("上传照片失败")

    table = readcsv('ManageMember_data.csv')

    @ddt.data(*table)
    def test_ManageMember(self,row):
        # 会员管理
        self.driver.find_element_by_link_text("会员管理").click()
        self.driver.find_element_by_link_text("添加会员").click()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('username').send_keys(row[0])
        self.driver.find_element_by_name('mobile_phone').clear()
        self.driver.find_element_by_name('mobile_phone').send_keys(row[1])
        if row[2] == 'M':
            self.driver.find_element_by_css_selector('[name="sex"][value="1"]').click()
        elif row[2] == 'F':
            self.driver.find_element_by_css_selector('[name="sex"][value="0"]').click()
        else:
            pass
        self.driver.find_element_by_id('birthday').clear()
        self.driver.find_element_by_id('birthday').send_keys(row[3])
        self.driver.find_element_by_name('email').clear()
        self.driver.find_element_by_name('email').send_keys(row[4])
        self.driver.find_element_by_name('qq').clear()
        self.driver.find_element_by_name('qq').send_keys(row[5])
        self.driver.find_element_by_class_name('button_search').click()
        time.sleep(3)
        WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,'#datagrid-row-r1-2-0 > td:nth-child(1) > div')))
        self.assertEqual(self.driver.find_element_by_css_selector('#datagrid-row-r1-2-0 > td:nth-child(1) > div').text,row[0])


if __name__ == '__main__':
    unittest2.main()