import datetime
import time

NO = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')[:-7]
print(NO)
time.sleep(3)
NO1 = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
print(NO1)
