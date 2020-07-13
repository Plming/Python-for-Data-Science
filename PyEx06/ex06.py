'''
Created on 2020. 7. 11.

@author: kim01
'''
f = open('./test.txt', 'a', encoding='utf-8')
# print(f)

f.write('hello1\n')
f.write('hello1\n')

print('성공')

f.close()