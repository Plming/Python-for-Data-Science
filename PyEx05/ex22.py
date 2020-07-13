'''
Created on 2020. 7. 10.

@author: kim01
'''
import os

print(os.path.abspath('.'))
print(os.getcwd())

# 경로를 나타내는 구분자
# 윈도우: \
# 리눅스: /
print(os.path.dirname('C:/Python/test.txt'))
print(os.path.basename('C:/Python/test.txt'))

print(os.listdir('C:/Python'))
print(os.listdir('.'))

print(os.path.exists('./ex21.py'))

# 파일 / 디렉토리
# os.path.isdir / os.path.isfile
print(os.path.isdir('./ex22.py'))
print(os.path.isdir('C:/Python'))

# 파일 사이즈(바이트 기준)
# k - 1024 / M - 1024*1024

print(os.path.getsize('C:/Python/test.txt'),'bytes')
