# coding=utf-8
import os
import ddt
import unittest2

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))

import sys
if PKG_DIR not in sys.path:
    sys.path.append(PKG_DIR)

from tools.csvmanager import readcsv
from script.ind_Base import ind_Base
from result.HTMLTestRunner import HTMLTestRunner


@ddt.ddt
class interface_get_information(ind_Base):
    def setUp(self):
        self.URL = f'{self.BaseURL}get_information.do'

    table = readcsv('ind', 'get_information_data.csv')
    @ddt.data(*table)
    def test_interface(self,i):
        self.request.post(f'{self.BaseURL}login.do',{'username':i[0],'password':i[1]})
        url = self.URL
        data = {}
        request = self.request.post(url,data).json()
        self.assertIn(str(i[7]),str(request['status']))
        self.assertIn(str(i[0]),str(request['data']['username']))
        self.assertIn(str(i[2]),str(request['data']['email']))
        self.assertIn(str(i[3]),str(request['data']['phone']))
        self.assertIn(str(i[4]),str(request['data']['question']))
        self.assertIn(str(i[5]),str(request['data']['answer']))
        self.assertIn(str(i[6]),str(request['data']['role']))



if __name__ == '__main__':
    suite = unittest2.defaultTestLoader.discover(CUR_DIR,'get_information.py')
    filePath = PKG_DIR.replace('script','result/ind_result/get_information_result.html')
    with open(filePath,'wb') as file:
        HTMLTestRunner(stream=file, verbosity=1, title='自动化测试报告', description='测试环境：Chrome', tester='YYJ').run(suite)