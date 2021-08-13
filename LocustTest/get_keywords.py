import os
import requests
from lxml import etree

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))

def get_keywords():
    url = 'https://localhost/iwebshop/index.php?controller=site&action=sitemap'
    data = {'controller':'site',
            'action':'sitemap'}
    res = requests.Session().get(url = url, data = data, verify = False)
    res.encoding="utf-8"
    listkeywords = []
    doc = etree.HTML(res.text)

    num1 = len(doc.xpath(f'/html/body/div[1]/div[6]/div[2]/div[3]/text()'))
    for i in range(1,num1):
        A=doc.xpath(f'/html/body/div[1]/div[6]/div[2]/div[3]/table[{i}]/tbody/tr[1]/th/a/text()')[0]
        listkeywords.append(A)
        num2 = len(doc.xpath(f'/html/body/div[1]/div[6]/div[2]/div[3]/table[{i}]/tbody/text()'))
        for j in range(2,num2-1):
            B=doc.xpath(f'/html/body/div[1]/div[6]/div[2]/div[3]/table[{i}]/tbody/tr[{j}]/th/a/text()')[0]
            listkeywords.append(B)
            num3 = len(doc.xpath(f'/html/body/div[1]/div[6]/div[2]/div[3]/table[{i}]/tbody/tr[{j}]/td/text()'))
            for k in range(1,num3):
                C=doc.xpath(f'/html/body/div[1]/div[6]/div[2]/div[3]/table[{i}]/tbody/tr[{j}]/td/a[{k}]/text()')[0]
                listkeywords.append(C)

    filePath = CUR_DIR+"\\"+"keywords.csv"
    with open(filePath, 'w') as f:
        for i in listkeywords:
            f.write(i+'\n')

get_keywords()