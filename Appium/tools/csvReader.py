import csv
import os


def readcsv(fileName):
    csvlist = []
    base_path = os.path.dirname(__file__)
    filePath = base_path.replace('tools','data/')+fileName
    with open(filePath, 'r') as f:
        table = csv.reader(f)
        i = 0
        for row in table:
            if i == 0:
                pass
            else:
                csvlist.append(row)
            i = i+1
    return csvlist