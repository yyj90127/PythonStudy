import os
import ddt
import unittest2

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))

import sys
if PKG_DIR not in sys.path:
    sys.path.append(PKG_DIR)

from tools.csvmanager import readcsv
from script.mul_Base import mul_Base
from result.HTMLTestRunner import HTMLTestRunner


# 针对多个接口联调测试
@ddt.ddt
class workflow_FPAndUI(mul_Base):

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
        self.assertIn(str(i[11]),str(request['status']))

    # 2、用户登录
    def login(self,i,password):
        url = self.BaseURL+"login.do"
        if password == 'passwordOld':
            password = i[1]
        else:
            password = i[10]
        data = {'username':i[0],'password':password}
        request = self.request.post(url,data=data).json()
        self.assertIn(str(i[11]),str(request['status']))

    # 3、修改个人信息
    def updateInformation(self,i):
        url = self.BaseURL + "update_information.do"
        data = {'email': i[2],
                'phone': i[3],
                'question': i[4],
                'answer': i[9]}
        request = self.request.post(url, data=data).json()
        self.assertIn(str(i[11]),str(request['status']))

    # 4、忘记密码，获取密保问题
    def forgetGetQuestion(self,i):
        url = self.BaseURL+"forget_get_question.do"
        data = {'username':i[0]}
        request = self.request.post(url,data=data).json()
        self.question = request['data']
        self.assertIn(str(i[11]),str(request['status']))

    # 5、提交密保问题答案
    def forgetCheckAnswer(self,i,question):
        url = self.BaseURL+"forget_check_answer.do"
        data = {'username':i[0],'question':question,'answer':i[9]}
        request = self.request.post(url,data=data).json()
        self.token = request['data']
        self.assertIn(str(i[11]),str(request['status']))

    # 6、回答完密保问题后修改密码
    def forgetResetPassword(self,i,token):
        url = self.BaseURL+"forget_reset_password.do"
        data = {'username':i[0],'passwordNew':i[10],'forgetToken':token}
        request = self.request.post(url,data=data).json()
        self.assertIn(str(i[11]),str(request['status']))

    table = readcsv('mul', 'FPAndUI_data.csv')
    @ddt.data(*table)
    def test_run(self,i):
        self.register(i)
        self.login(i,'passwordOld')
        self.updateInformation(i)
        self.forgetGetQuestion(i)
        self.forgetCheckAnswer(i,self.question)
        self.forgetResetPassword(i,self.token)
        self.login(i,'passwordNew')



if __name__ == '__main__':
    suite = unittest2.defaultTestLoader.discover(CUR_DIR,'workflow_FPAndUI.py')
    filePath = PKG_DIR.replace('script','result/mul_result/FPAndUI_result.html')
    with open(filePath,'wb') as file:
        HTMLTestRunner(stream=file, verbosity=1, title='自动化测试报告', description='测试环境：Chrome', tester='YYJ').run(suite)