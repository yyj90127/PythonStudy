import os
import ddt
import unittest2

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))

import sys
if PKG_DIR not in sys.path:
    sys.path.append(PKG_DIR)

from tools.csvmanager import readcsv
from result.HTMLTestRunner import HTMLTestRunner
from script.mul_Base import mul_Base


# 针对多个接口联调测试
@ddt.ddt
class workflow_updateInformation(mul_Base):

    # 1、用户注册
    def register(self,i):
        url = self.BaseURL+"register.do"
        data = {'username':i[0],
                'password':i[1],
                'email':i[2],
                'phone':i[3],
                'question':i[4],
                'answer':i[5]}
        request = self.request.post(url,data=data).json()
        self.assertIn(str(i[10]),str(request['status']))

    # 2、用户登录
    def login(self,i):
        url = self.BaseURL+"login.do"
        data = {'username':i[0],'password':i[1]}
        request = self.request.post(url,data=data).json()
        self.assertIn(str(i[10]),str(request['status']))

    # 3、获取用户信息
    def getInformation(self,i,round):
        url = self.BaseURL+"get_information.do"
        data = {}
        request = self.request.post(url,data=data).json()
        if round == 1:
            self.assertIn(str(i[10]),str(request['status']))
        else:
            self.assertIn(str(i[10]),str(request['status']))
            self.assertIn(str(i[6]),str(request['data']['email']))
            self.assertIn(str(i[7]),str(request['data']['phone']))
            self.assertIn(str(i[8]),str(request['data']['question']))
            self.assertIn(str(i[9]),str(request['data']['answer']))

    # 4、修改个人信息
    def updateInformation(self,i):
        url = self.BaseURL + "update_information.do"
        data = {'email': i[6],
                'phone': i[7],
                'question': i[8],
                'answer': i[9]}
        request = self.request.post(url, data=data).json()
        self.assertIn(str(i[10]),str(request['status']))

    table = readcsv('mul', 'update_Information_data.csv')
    @ddt.data(*table)
    def test_run(self,i):
        self.register(i)
        self.login(i)
        self.getInformation(i,1)
        self.updateInformation(i)
        self.getInformation(i,2)



if __name__ == '__main__':
    suite = unittest2.defaultTestLoader.discover(CUR_DIR,'workflow_updateInformation.py')
    filePath = PKG_DIR.replace('script','result/mul_result/updateInformation_result.html')
    with open(filePath,'wb') as file:
        HTMLTestRunner(stream=file, verbosity=1, title='自动化测试报告', description='测试环境：Chrome', tester='YYJ').run(suite)