import csv
import os


def readcsv(fileName):
    csvlist = []
    base_path = os.path.dirname(__file__)
    filePath = base_path.replace('tools','data/')+fileName
    with open(filePath, 'r', encoding = "utf-8") as f:
        table = csv.reader(f)
        header = next(table)
        for row in table:
            csvlist.append(row)
    return csvlist