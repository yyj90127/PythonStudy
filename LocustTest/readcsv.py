import csv
import os

def readcsv(fileName):
    list = []
    base_path = os.path.dirname(__file__)
    filePath = base_path+"\\"+fileName
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