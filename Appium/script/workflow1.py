import os
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from config.caps import get_caps
from tools.csvReader import readcsv

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))
filename = "workflow1_result.csv"
filepath = PKG_DIR+"/result/"+filename


class workflow1(object):

    def addnote(self,driver,title,num):
        if int(num) == 1:
            WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'android:id/button1'))).click()
            WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/indicator_2')))
            driver.swipe(1000,1000,100,1000)
            WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/enter_app'))).click()
        WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/add_note'))).click()
        WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/add_note_floater_add_note'))).click()
        if int(num) == 1:
            WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/btn_cancel'))).click()
        WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/note_title'))).send_keys(title)
        WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@resource-id='com.youdao.note:id/note_content']/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView"))).click()
        WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/actionbar_complete_text'))).click()

    def check_addnote(self,driver,title):
        with open(filepath,"a") as f:
            result = WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/title'))).text
            if result == title:
                f.write(title+"：新增测试成功"+"\n")
            else:
                f.write(title+"：新增测试失败"+"\n")

    def searchnote(self,driver,title):
        WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/search'))).click()
        WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/search_edit_view'))).send_keys(title)
        WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/clear_search_text_btn'))).click()

    def check_searchnote(self,driver,title):
        # 获取截图
        driver.get_screenshot_as_file(f'{PKG_DIR}/result/{title}.png')

    def editnote(self,driver,edit):
        WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/title'))).click()
        WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/edit'))).click()
        WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/note_title'))).send_keys(edit)
        WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/actionbar_complete_text'))).click()

    def check_editnote(self,driver,title):
        with open(filepath,"a") as f:
            result = WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/note_title'))).text
            if result == title:
                f.write(title+"：编辑测试成功"+"\n")
            else:
                f.write(title+"：编辑测试失败"+"\n")

    def delnote(self,driver):
        WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/menu_more'))).click()
        WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/delete'))).click()
        WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/btn_ok'))).click()
        driver.keyevent(4)

    def check_delnote(self,driver,title):
        with open(filepath,"a") as f:
            result = WebDriverWait(driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/empty_text'))).text
            if result == "当前列表中没有文档":
                f.write(title+"：删除测试成功"+"\n")
            else:
                f.write(title+"：删除测试失败"+"\n")

    def delresult(self):
        # 删除以png结尾的所有文件
        pngfilepath = PKG_DIR+"/result/"
        for root, dirs, files in os.walk(pngfilepath):
            for name in files:
                if name.endswith(".png"):
                    os.remove(os.path.join(root, name))
        # 删除测试报告文件
        if os.path.exists(filepath):
            os.remove(filepath)

    def run(self):
        caps = get_caps()
        self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', caps)
        self.delresult()
        table = readcsv("workflow_data.csv")
        for i in table:
            self.addnote(self.driver,i[1],i[0])
            self.check_addnote(self.driver,i[1])
            self.searchnote(self.driver,i[1])
            self.check_searchnote(self.driver,i[1])
            self.editnote(self.driver,i[2])
            self.check_editnote(self.driver,i[2])
            self.delnote(self.driver)
            self.check_delnote(self.driver,i[2])
        self.driver.quit()


if __name__ == '__main__':
    workflow1().run()