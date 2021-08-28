import os
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))


class addnote:
    def __init__(self):
        self.caps = {}
        self.caps['automationName'] = 'UiAutomator2'
        self.caps['platformName'] = 'Android'
        self.caps['platformVersion'] = '8.0'
        self.caps['deviceName'] = '28d2e631'
        self.caps['appPackage'] = 'com.zhongan.iyunbao'
        self.caps['appActivity'] = '.IybSplashActivity'
        self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', self.caps)

    def openhbt(self):
        WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.zhongan.iyunbao:id/positive'))).click()
        WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'android:id/button1'))).click()
        WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.zhongan.iyunbao:id/tv_skip'))).click()
        WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'android:id/button1'))).click()
        # print(WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@resource-id ='com.zhongan.iyunbao:id/tab_bottom']/android.widget.LinearLayout/android.widget.RelativeLayout/[@resource-id ='com.zhongan.iyunbao:id/content']/[@resource-id ='com.zhongan.iyunbao:id/custom_tab_text']"))).text)
        # WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@resource_id ='com.zhongan.iyunbao:id/tab_bottom']/android.widget.LinearLayout/[@class='android.widget.RelativeLayout' and @index='4']"))).click()
        # self.driver.quit()

if __name__ == '__main__':
    addnote().openhbt()