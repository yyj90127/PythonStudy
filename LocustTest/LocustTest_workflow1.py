# 对登录功能进行单点性能测试（一组测试数据）
import datetime
import os
import random
import urllib3

from get_keywords import get_keywords
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
    @task(1)
    def test_reg(self):
        # 发送首页请求到服务器 get,post
        # 这里地址写的是子目录的地址，空目录用"/"代替
        TestURL = '/index.php?controller=simple&action=reg_act'
        table = readcsv('reg_data.csv')
        for i in table:
            TestData = {
                "callback":"",
                "email":i[0],
                "username":i[1],
                "password":i[2],
                "repassword":i[2],
                "captcha":"11111"
            }
            res = self.client.post(url = TestURL, data = TestData, verify = False).text
            A = res.find("恭喜")
            filepath = CUR_DIR+"\\"+"reg_result.csv"
            with open(filepath,"a") as f:
                if A != -1:
                    f.write(f'{datetime.datetime.now()},“{i[0]}”注册成功'+'\n')
                else:
                    f.write(f'{datetime.datetime.now()},“{i[0]}”注册失败'+'\n')

    @task(1)
    def test_login(self):
        # 发送首页请求到服务器 get,post
        # 这里地址写的是子目录的地址，空目录用"/"代替
        TestURL = '/index.php?controller=simple&action=login_act'
        table = readcsv('login_data.csv')
        for i in table:
            TestData = {"callback":"",
                        "login_info":i[0],
                        "password":i[1]}
            res = self.client.post(url = TestURL, data = TestData, verify = False).text
            A = res.find(i[0])
            filepath = CUR_DIR+"\\"+"login_result.csv"
            with open(filepath,"a") as f:
                if A != -1:
                    f.write(f'{datetime.datetime.now()},“{i[0]}”登录成功'+'\n')
                else:
                    f.write(f'{datetime.datetime.now()},“{i[0]}”登录失败'+'\n')

    @task(8)
    def test_search(self):
        # 发送首页请求到服务器 get,post
        # 这里地址写的是子目录的地址，空目录用"/"代替
        listkeywords  = readcsv("keywords.csv")
        keyword = random.choice(listkeywords)[0]
        TestURL = f'/index.php?controller=site&action=search_list&word={keyword}'
        res = self.client.get(url = TestURL, verify = False).text
        A = res.find(f'"<span class="red">{keyword}</span>"搜索结果')
        filepath = CUR_DIR+"\\"+"search_result.csv"
        with open(filepath,"a") as f:
            if A != -1:
                f.write(f'{datetime.datetime.now()},“{keyword}”测试成功'+'\n')
            else:
                f.write(f'{datetime.datetime.now()},“{keyword}”测试失败'+'\n')

    # tasks = {test_login:1,test_search:4}

class WebSiteUser(HttpLocust):
    # 若已存在同名的文档，则先删除文档
    filenamelist = ["reg_result.csv","login_result.csv","search_result.csv"]
    for filename in filenamelist:
        if os.path.exists(filename):
            os.remove(filename)
    # 使用main方法无法调用get_keywords()，使用终端运行可以
    get_keywords()
    host = "https://localhost/iwebshop"
    task_set = UserBehavior
    # 最短等待时间（毫秒）
    min_wait = 2000
    # 最长等待时间（毫秒）
    max_wait = 5000


if __name__ == '__main__':
    file_path = os.path.abspath(__file__)
    os.system(f'locust -f {file_path} --web-host=127.0.0.1')