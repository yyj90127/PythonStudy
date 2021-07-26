import csv
import os


def readcsv(type, fileName = None):
    list = []
    base_path = os.path.abspath(os.path.dirname(__file__))
    if type == 'ind':
        filePath = base_path.replace('tools','data/ind_data/') + fileName
    elif type == 'mul':
        filePath = base_path.replace('tools', 'data/mul_data/') + fileName
    elif type == 'url':
        filePath = base_path.replace('tools', 'config/url.csv')

    with open(filePath, 'r', encoding='utf-8') as f:
        table = csv.reader(f)
        i = 0
        for row in table:
            if i == 0:
                pass
            else:
                list.append(row)
            i = i+1
    return list