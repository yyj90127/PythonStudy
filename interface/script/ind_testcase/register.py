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
class interface_register(ind_Base):
    def setUp(self):
        self.URL = f'{self.BaseURL}register.do'

    table = readcsv('ind', 'register_data.csv')
    @ddt.data(*table)
    def test_interface(self, i):
        url = self.URL
        data = {'username': i[0],
                'password': i[1],
                'email': i[2],
                'phone': i[3],
                'question': i[4],
                'answer': i[5]}
        request = self.request.post(url, data).json()
        self.assertIn(str(i[6]),str(request['status']))



if __name__ == '__main__':
    suite = unittest2.defaultTestLoader.discover(CUR_DIR,'register.py')
    filePath = PKG_DIR.replace('script','result/ind_result/register_result.html')
    with open(filePath,'wb') as file:
        HTMLTestRunner(stream=file, verbosity=1, title='自动化测试报告', description='测试环境：Chrome', tester='YYJ').run(suite)