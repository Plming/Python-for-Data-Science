'''
Created on 2020. 7. 10.

@author: kim01
'''
import time

# UNIX 시간
print(time.time())
print(time.localtime(time.time()))

# 부분시간 추출
print(time.asctime(time.localtime(time.time())))
print(time.ctime())

# 시스템에 의존적
print(time.strftime('%x',time.localtime()))
print(time.strftime('%c',time.localtime()))