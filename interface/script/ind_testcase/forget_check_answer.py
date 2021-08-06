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
class interface_forget_check_answer(ind_Base):
    def setUp(self):
        self.URL = f'{self.BaseURL}forget_check_answer.do'

    table = readcsv('ind', 'forget_check_answer_data.csv')
    @ddt.data(*table)
    def test_interface(self,i):
        self.request.post(f'{self.BaseURL}login.do',{'username':i[0],'password':i[1]})
        url = self.URL
        data = {'username':i[0],
                'question':i[2],
                'answer':i[3]}
        request = self.request.post(url,data).json()
        self.assertIn(str(i[4]),str(request['status']))



if __name__ == '__main__':
    suite = unittest2.defaultTestLoader.discover(CUR_DIR,'forget_check_answer.py')
    filePath = PKG_DIR.replace('script','result/ind_result/forget_check_answer_result.html')
    with open(filePath,'wb') as file:
        HTMLTestRunner(stream=file, verbosity=1, title='自动化测试报告', description='测试环境：Chrome', tester='YYJ').run(suite)