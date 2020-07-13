'''
Created on 2020. 7. 11.

@author: kim01
'''

# 윈도우 기본 인코딩은 cp949이다.
# 따라서 utf-8로 인코딩을 바꾸어야 함
f = open('./test.txt', 'w', encoding='utf-8')

f.write('hello\n')
f.write('한글\n')

f.close()
