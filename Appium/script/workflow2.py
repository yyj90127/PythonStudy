import unittest
import ddt
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from config.caps import get_caps
from script.workflow1 import workflow1
from tools.csvReader import readcsv


@ddt.ddt
class workflow2(unittest.TestCase,workflow1):
    @classmethod
    def setUpClass(cls):
        caps = get_caps()
        cls.driver = WebDriver('http://127.0.0.1:4723/wd/hub', caps)
        workflow1().delresult()

    table = readcsv("workflow_data.csv")
    @ddt.data(*table)
    def test_case1(self,i):
        workflow1().addnote(self.driver,i[1],i[0])
        addnoteResult = WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/title'))).text
        self.assertEqual(i[1],addnoteResult)
        workflow1().searchnote(self.driver,i[1])
        workflow1().check_searchnote(self.driver,i[1])
        workflow1().editnote(self.driver,i[2])
        editnoteResult = WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/note_title'))).text
        self.assertEqual(i[2],editnoteResult)
        workflow1().delnote(self.driver)
        delnoteResult = WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.youdao.note:id/empty_text'))).text
        self.assertEqual("当前列表中没有文档",delnoteResult)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main()