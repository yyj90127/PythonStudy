# 对登录功能进行单点性能测试（一组测试数据）
import datetime
import os
import requests
import urllib3
from readcsv import readcsv
from locust import HttpLocust, task, TaskSet, events
from gevent._semaphore import Semaphore

urllib3.disable_warnings()
CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))
all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()

def on_hatch_complete(**kwargs):
    all_locusts_spawned.release() # 创建钩子方法

# 挂在到locust钩子函数（所有的Locust示例产生完成时触发）
# 1.0之前的写法
events.hatch_complete += on_hatch_complete
# 1.0之后的写法
# events.spawning_complete.add_listener(on_hatch_complete)

# 定义测试类：用户行为
class UserBehavior(TaskSet):
    # 设置集合点
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        # 限制在所有用户准备完成前处于等待状态
        all_locusts_spawned.wait()

    # 指定测试任务
    @task
    def test_usercenter(self):
        # 发送首页请求到服务器 get,post
        # 这里地址写的是子目录的地址，空目录用"/"代替
        table = readcsv('login_data.csv')
        for i in table:
            logincookie = login(i[0],i[1])
            TestURL = '/index.php?controller=ucenter'
            TestData = {"controller":"ucenter"}
            TestHeaders = {"Cookie":logincookie}
            res = self.client.get(url = TestURL, data = TestData, headers = TestHeaders, verify = False).text
            A = res.find(f"您好，{i[0]} 欢迎回来!")
            filepath = CUR_DIR+"\\"+"usercenter_result.csv"
            with open(filepath,"a") as f:
                if A != -1:
                    f.write(f'{datetime.datetime.now()},“{i[0]}”打开个人中心成功'+'\n')
                else:
                    f.write(f'{datetime.datetime.now()},“{i[0]}”打开个人中心失败'+'\n')

class WebSiteUser(HttpLocust):
    # 若已存在同名的文档，则先删除文档
    filenamelist = ["usercenter_result.csv"]
    for filename in filenamelist:
        if os.path.exists(filename):
            os.remove(filename)
    host = "https://localhost/iwebshop"
    task_set = UserBehavior
    # 最短等待时间（毫秒）
    min_wait = 2000
    # 最长等待时间（毫秒）
    max_wait = 5000

def login(username,password):
    TestURL = 'https://localhost/iwebshop/index.php?controller=simple&action=login_act'
    TestData = {"callback":"",
                "login_info":username,
                "password":password}
    res = dict(requests.post(url = TestURL, data = TestData, verify = False).cookies)
    logincookie = ''
    for k,v in res.items():
        logincookie = logincookie+(f'{k}={v}')+"; "
    return logincookie


if __name__ == '__main__':
    file_path = os.path.abspath(__file__)
    os.system(f'locust -f {file_path} --web-host=127.0.0.1')