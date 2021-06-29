import csv
import os


def readcsv(fileName):
    list = []
    # filePath = '../test_data/'+fileName
    # filePath = 'D:/Script/python/study/Selenium/test_data/register_data.csv'
    base_path = os.path.dirname(__file__)
    filePath = base_path.replace('test_tools','test_data/')+fileName
    with open(filePath, 'r') as f:
        table = csv.reader(f)
        i = 0
        for row in table:
            if i == 0:
                pass
            else:
                list.append(row)
            i = i+1
    return list