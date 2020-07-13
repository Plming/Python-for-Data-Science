'''
Created on 2020. 7. 11.

@author: kim01
'''
# zipsearch01.py

file = open('./zipcode_all_utf8_type2.csv', 'r', encoding='utf-8')

inputData = input('동 이름 입력:')

while len(inputData) < 2:
    inputData = input('동 이름 입력:')

while True:
    line = file.readline()
    
    if not line:
        break;
    
    data = line.split(sep=',')
    if data[3].startswith(inputData):
        print('[',data[0],']',data[1],data[2],data[3],data[4],data[5])

file.close()
