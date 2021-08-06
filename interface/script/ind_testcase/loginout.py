# coding=utf-8
import os
import unittest2

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))

import sys
if PKG_DIR not in sys.path:
    sys.path.append(PKG_DIR)

from script.ind_Base import ind_Base
from result.HTMLTestRunner import HTMLTestRunner


class interface_loginout(ind_Base):
    def setUp(self):
        self.URL = f'{self.BaseURL}loginout.do'

    def test_interface(self):
        url = self.URL
        request = self.request.get(url).json()
        self.assertIn("0",str(request['status']))



if __name__ == '__main__':
    suite = unittest2.defaultTestLoader.discover(CUR_DIR,'loginout.py')
    filePath = PKG_DIR.replace('script','result/ind_result/loginout_result.html')
    with open(filePath,'wb') as file:
        HTMLTestRunner(stream=file, verbosity=1, title='自动化测试报告', description='测试环境：Chrome', tester='YYJ').run(suite)