'''
Created on 2020. 7. 10.

@author: kim01
'''
import os

# system path
# program이 시작할 때 설정
print(os.environ['PATH'])
print(os.environ['PYTHONPATH'])

# current working directory 현재 작업 디렉토리
print(os.getcwd())
os.chdir('C:/Python')
print(os.getcwd())