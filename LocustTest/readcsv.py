import csv
import os

def readcsv(fileName):
    list = []
    base_path = os.path.dirname(__file__)
    filePath = base_path+"\\"+fileName
    with open(filePath, 'r') as f:
        table = csv.reader(f)
        header = next(table)
        for row in table:
            list.append(row)
    return list