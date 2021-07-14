import requests
from interface.tools.csvmanager import readcsv

# 针对多个接口联调测试
class workflow_forgetPassword(object):
    def __init__(self):
        self.BaseURL = 'http://localhost:8081/jwshoplogin/user/'

    # 读取文件
    def getdata(self):
        list = []
        table = readcsv('register_data.csv')
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
        request = requests.session().post(url,data=data).json()
        result = (request['status'])
        if result == 0:
            return f'用户”{i[0]}“注册成功'
        else:
            return f'用户”{i[0]}“注册失败'

    # 2、用户登录
    def test_login(self,i,passwordNew):
        url = self.BaseURL+"login.do"
        if passwordNew == 'passwordOld':
            password = i[1]
        else:
            password = i[6]
        data = {'username':i[0],'password':password}
        request = requests.session().post(url,data=data).json()
        result = (request['status'])
        if result == 0:
            return f'用户"{i[0]}"登录成功'
        else:
            return f'用户"{i[0]}"登录失败'

    # 3、忘记密码，获取密保问题
    def test_forgetGetQuestion(self,i):
        url = self.BaseURL+"forget_get_question.do"
        data = {'username':i[0]}
        request = requests.session().post(url,data=data).json()
        result = (request['status'])
        if result == 0:
            return request['data']
        else:
            return request['msg']

    # 4、提交密保问题答案
    def test_forgetCheckAnswer(self,i,question):
        url = self.BaseURL+"forget_check_answer.do"
        data = {'username':i[0],'question':question,'answer':i[5]}
        request = requests.session().post(url,data=data).json()
        result = (request['status'])
        if result == 0:
            return request['data']
        else:
            return request['msg']

    # 5、回答完密保问题后修改密码
    def test_forgetResetPassword(self,i,token):
        url = self.BaseURL+"forget_reset_password.do"
        data = {'username':i[0],'passwordNew':i[6],'forgetToken':token}
        request = requests.session().post(url,data=data).json()
        result = (request['status'])
        if result == 0:
            return request['msg']
        else:
            return request['msg']


    def run(self):
        filePath = r'D:\Script\python\study\interface\data\result.csv'
        with open(filePath,'w') as f:
            for i in self.getdata():
                f.write(self.test_register(i)+'\n')
                f.write(self.test_login(i,'passwordOld')+'\n')
                question = self.test_forgetGetQuestion(i)
                f.write(question+'\n')
                token = self.test_forgetCheckAnswer(i,question)
                f.write(token+'\n')
                f.write(self.test_forgetResetPassword(i,token)+'\n')
                f.write(self.test_login(i,'passwordNew')+'\n')
                f.write('\n')



if __name__ == '__main__':
    obj = workflow_forgetPassword()
    obj.run()