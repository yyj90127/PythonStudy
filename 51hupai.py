from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://moni.51hupai.org/')
area = driver.find_element_by_id("changehistory")
Select(area).select_by_value("2107")
A = driver.find_element_by_css_selector("#root > div > div.whomemain > div > div.whbiddingcontent > div.whbiddingitem.whbiddingleft > div.whpubinfo > div > div.detail-proinfo.secdetail-proinfo > span:nth-child(4) > span")
while A.text <= '11:29:59':
    A = driver.find_element_by_css_selector("#root > div > div.whomemain > div > div.whbiddingcontent > div.whbiddingitem.whbiddingleft > div.whpubinfo > div > div.detail-proinfo.secdetail-proinfo > span:nth-child(4) > span")
    B = driver.find_element_by_css_selector("#root > div > div.whomemain > div > div.whbiddingcontent > div.whbiddingitem.whbiddingleft > div.whpubinfo > div > div.detail-proinfo.secdetail-proinfo > span:nth-child(6) > span")
    if A.text <= '11:29:59' and A.text >= '11:29:40':
        print(A.text,B.text)
    time.sleep(0.9)
    try:
        A = driver.find_element_by_css_selector("#root > div > div.whomemain > div > div.whbiddingcontent > div.whbiddingitem.whbiddingleft > div.whpubinfo > div > div.detail-proinfo.secdetail-proinfo > span:nth-child(4) > span")
    except BaseException:
        break

time.sleep(1)
C = driver.find_element_by_css_selector("#root > div > div.whomemain > div > div.whbiddingcontent > div.whbiddingitem.whbiddingleft > div.whpubinfo > div > div > p:nth-child(3)")
print('11:30:00',C.text[6:])
driver.quit()