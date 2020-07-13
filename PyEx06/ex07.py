'''
Created on 2020. 7. 11.

@author: kim01
'''
# read 모드는 파일이 없을 경우 에러 발생
# 파일이 존재하는지 검사하고 써야함

# if / try ~ except

f = open('./test.txt', 'r', encoding='utf-8')

# line = f.readline()
# print(line,end='')
# line = f.readline()
# print(line,end='')

while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')

f.close()
