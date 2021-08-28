import csv
import os


def readcsv(fileName):
    csvlist = []
    # filePath = '../test_data/'+fileName
    # filePath = 'D:/Script/python/study/Selenium/test_data/register_data.csv'
    base_path = os.path.dirname(__file__)
    filePath = base_path.replace('test_tools','test_data/')+fileName
    with open(filePath, 'r') as f:
        table = csv.reader(f)
        header = next(table)
        for row in table:
            csvlist.append(row)
    return csvlist