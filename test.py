import time
import datetime

t = time.time()

print (int(round(t * 1000)))    #毫秒级时间戳

now_time = datetime.datetime.now()
A = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')[:-7]
print(A)