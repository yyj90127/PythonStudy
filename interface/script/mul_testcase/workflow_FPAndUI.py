import os
import requests

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))

import sys
if PKG_DIR not in sys.path:
    sys.path.append(PKG_DIR)

from interface.tools.csvmanager import readcsv

# 针对多个接口联调测试
class workflow_FPAndUI():
    def __init__(self):
        list = []
        table = readcsv('url')
        for i in table:
            list.append(i)
        self.BaseURL = f'{list[0][0]}'
        self.request = requests.session()

    # 读取文件
    def getdata(self):
        list = []
        table = readcsv('mul', 'FPAndUI_data.csv')
        for i in table:
            list.append(i)
        return list

    # 1、用户注册
    def test_register(self,i):
        url = self.BaseURL+"register.do"
        data = {'username':i[0],
                'password':i[1],
                'email':i[2],
                'phone':i[3],
                'question':i[4],
                'answer':i[5]}
        request = self.request.post(url,data=data).json()
        result = (request['status'])
        if result == 0:
            return f'用户”{i[0]}“注册成功'
        else:
            return f'用户”{i[0]}“注册失败'

    # 2、用户登录
    def test_login(self,i,password):
        url = self.BaseURL+"login.do"
        if password == 'passwordOld':
            password = i[1]
        else:
            password = i[10]
        data = {'username':i[0],'password':password}
        request = self.request.post(url,data=data).json()
        result = (request['status'])
        if result == 0:
            return f'用户"{i[0]}"登录成功'
        else:
            return f'用户"{i[0]}"登录失败'

    # 3、修改个人信息
    def test_updateInformation(self,i):
        url = self.BaseURL + "update_information.do"
        data = {'email': i[2],
                'phone': i[3],
                'question': i[4],
                'answer': i[9]}
        request = self.request.post(url, data=data).json()
        result = (request['status'])
        if result == 0:
            return f'用户"{i[0]}"修改个人信息成功'
        else:
            return f'用户"{i[0]}"修改个人信息失败'

    # 4、忘记密码，获取密保问题
    def test_forgetGetQuestion(self,i):
        url = self.BaseURL+"forget_get_question.do"
        data = {'username':i[0]}
        request = self.request.post(url,data=data).json()
        result = (request['status'])
        self.question = request['data']
        if result == 0:
            return f'用户"{i[0]}"获取密保问题成功'
        else:
            return f'用户"{i[0]}"获取密保问题失败'

    # 5、提交密保问题答案
    def test_forgetCheckAnswer(self,i,question):
        url = self.BaseURL+"forget_check_answer.do"
        data = {'username':i[0],'question':question,'answer':i[9]}
        request = self.request.post(url,data=data).json()
        result = (request['status'])
        self.token = request['data']
        if result == 0:
            return f'用户"{i[0]}"获取token成功'
        else:
            return f'用户"{i[0]}"获取token失败'

    # 6、回答完密保问题后修改密码
    def test_forgetResetPassword(self,i,token):
        url = self.BaseURL+"forget_reset_password.do"
        data = {'username':i[0],'passwordNew':i[10],'forgetToken':token}
        request = self.request.post(url,data=data).json()
        result = (request['status'])
        if result == 0:
            return f'用户"{i[0]}"修改密码成功'
        else:
            return f'用户"{i[0]}"修改密码失败'


    def run(self):
        filePath = PKG_DIR.replace('script', 'result/mul_result/FPAndUI_result.csv')
        with open(filePath,'w',encoding='utf-8') as f:
            for i in self.getdata():
                f.write(self.test_register(i)+'\n'+
                        self.test_login(i,'passwordOld')+'\n'+
                        self.test_updateInformation(i)+'\n'+
                        self.test_forgetGetQuestion(i)+'\n'+
                        self.test_forgetCheckAnswer(i,self.question)+'\n'+
                        self.test_forgetResetPassword(i,self.token)+'\n'+
                        self.test_login(i,'passwordNew')+'\n'+
                        '\n')



if __name__ == '__main__':
    obj = workflow_FPAndUI()
    obj.run()

