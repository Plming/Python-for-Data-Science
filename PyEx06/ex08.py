'''
Created on 2020. 7. 11.

@author: kim01
'''

f = open('./test.txt', 'r', encoding='utf-8')

lines = f.readlines()

# print(type(lines))
# print(lines)

for line in lines:
    print(line, end='')

f.close()
