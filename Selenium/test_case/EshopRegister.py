import os
import sys
CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))
if PKG_DIR not in sys.path:
    sys.path.append(PKG_DIR)

import unittest2
from test_case.BaseTestCase import setUpClassAndtearDownClass
from test_tools.csvFilesManager import readcsv
import ddt

@ddt.ddt
class Register(setUpClassAndtearDownClass):

    def setUp(self):
        self.driver.get('http://localhost/index.php?m=user&c=public&a=reg')

    def tearDown(self):
        pass

    table = readcsv('register_data.csv')

    @ddt.data(*table)
    def test_Register(self,row):
        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('username').send_keys(row[0])
        self.driver.find_element_by_name('password').clear()
        self.driver.find_element_by_name('password').send_keys(row[1])
        self.driver.find_element_by_name('userpassword2').clear()
        self.driver.find_element_by_name('userpassword2').send_keys(row[2])
        self.driver.find_element_by_name('mobile_phone').clear()
        self.driver.find_element_by_name('mobile_phone').send_keys(row[3])
        self.driver.find_element_by_name('email').clear()
        self.driver.find_element_by_name('email').send_keys(row[4])
        # self.driver.find_element_by_css_selector('[value="注册"]').click()


if __name__ == '__main__':
    unittest2.main()