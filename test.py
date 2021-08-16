import csv

file1 = open("aaa.csv","r")
rows = csv.writer(file1)
file2 = open("bbb.csv","w",newline = '')
writer = csv.writer(file2)
for row in rows:
    row.append("测试通过")
    writer.writerow(row)

file1.close()
file2.close()