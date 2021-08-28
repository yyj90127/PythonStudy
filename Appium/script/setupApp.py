import os
import time

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))

class yd_install_removeV1:
    def __init__(self):
        self.caps = {}
        self.caps['automationName'] = 'UiAutomator2'
        self.caps['platformName'] = 'Android'
        self.caps['platformVersion'] = '8.0'
        self.caps['deviceName'] = '28d2e631'
        self.caps['appPackage'] = 'com.miui.home'
        self.caps['appActivity'] = '.launcher.Launcher'
        self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', self.caps)

    def test_install_remove(self):
        if self.driver.is_app_installed('com.youdao.note'):
            self.driver.remove_app('com.youdao.note')
        filename = "youdaoyunbiji.apk"
        filepath = PKG_DIR+"/tools/"+filename
        self.driver.install_app(filepath)

    def check_install(self):
        # S1：安装后用程序启动有道云
        self.caps['appPackage'] = 'com.youdao.note'
        self.caps['appActivity'] = '.activity2.MainActivity t3462'
        self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', self.caps)
        # S2：弹出界面上抓取“拒绝”链接
        # time.sleep(3)
        # el = self.driver.find_element_by_id('com.android.packageinstaller:id/permission_deny_button').is_enabled()

        el=WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_id('com.android.packageinstaller:id/permission_deny_button'))
        #print(el)
        # S3：如果链接存在的，那么打印“安装成功”
        # S4：否则打印安装失败
        if el:
            print("安装成功")
        else:
            print("安装失败")

if __name__ == '__main__':
    #初始化类的对象
    yd_install_remove_Obj=yd_install_removeV1()
    #调用卸载安装
    yd_install_remove_Obj.test_install_remove()
    #调用检查安装
    yd_install_remove_Obj.check_install()
