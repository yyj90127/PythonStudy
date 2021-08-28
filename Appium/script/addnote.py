import os
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from tools.csvReader import readcsv

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))
filename = "addnote_result.csv"
filepath = PKG_DIR+"/result/"+filename

class addnote:
    def __init__(self):
        self.caps = {}
        self.caps['automationName'] = 'UiAutomator2'
        self.caps['platformName'] = 'Android'
        self.caps['platformVersion'] = '8.0'
        self.caps['deviceName'] = '28d2e631'
        self.caps['appPackage'] = 'com.youdao.note'
        self.caps['appActivity'] = '.activity2.MainActivity'
        self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', self.caps)

    def addnote(self,title,num):
        if num == 0:
            WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'android:id/button1'))).click()
            WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/indicator_2')))
            self.driver.swipe(1000,1000,100,1000)
            WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/enter_app'))).click()
        WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/add_note'))).click()
        WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/add_note_floater_add_note'))).click()
        if num == 0:
            WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/btn_cancel'))).click()
        WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/note_title'))).send_keys(title)
        WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@resource-id='com.youdao.note:id/note_content']/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView"))).click()
        WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/actionbar_complete_text'))).click()

    def check_addnote(self,title):
        with open(filepath,"a") as f:
            result = WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/title'))).text
            if result == title:
                f.write(title+"：测试成功"+"\n")
            else:
                f.write(title+"：测试失败"+"\n")

    def run(self):
        if os.path.exists(filepath):
            os.remove(filepath)
        table = readcsv("addnote_data.csv")
        num = 0
        for i in table:
            self.addnote(i[0],num)
            self.check_addnote(i[0])
            num = num+1
        self.driver.quit()

if __name__ == '__main__':
    addnote().run()