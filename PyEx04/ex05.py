'''
Created on 2020. 7. 9.

@author: kim01
'''

# hong gil dong -> Hong Gil Dong
# 이름 입력

name = input('이름 입력:')

data = name.split(sep=' ')

result = []
for datum in data:
    result.append(datum.capitalize())
    
print('이름:', ' '.join(result))
