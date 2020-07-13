'''
Created on 2020. 7. 10.

@author: kim01
'''
import sys

# sys.path는 리스트의 형태이다

list = sys.path
print(list[0])

sys.path.append('C:\Python')
print(sys.path)
