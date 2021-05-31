import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
# 현재 시간
print(time.ctime())
print(time.strftime('(%A) %Y/%m/%d %H:%M:%S', time.localtime(time.time())))