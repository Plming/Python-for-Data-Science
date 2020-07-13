'''
Created on 2020. 7. 9.

@author: kim01
'''
# mod1.py 불러오기
# import mod1

# print(mod1.add(10, 20))
# print(mod1.sub(10, 20))

from mod1 import add, sub

# from mod1 import * : 모듈의 모든 것을 갖고오기 때문에 X

print(add(10, 20))
print(sub(10, 20))

from mod2 import add, sub

print(add(10, 20))
print(sub(10, 20))
