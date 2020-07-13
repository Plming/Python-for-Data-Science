'''
Created on 2020. 7. 10.

@author: kim01
'''
import os

location='C:/Python'
data=os.listdir(location)

for datum in data:
    if os.path.isdir(location+'/'+datum)==True:
        print('['+datum+']')
    else:
        print(datum)