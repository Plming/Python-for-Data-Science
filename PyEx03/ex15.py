'''
Created on 2020. 7. 8.

@author: kim01
'''
# 현대 프로그램 문법: 일급함수(함수의 정의를 값 취급)
# C언어 -> 함수 포인터
# javascript
# 함수를 객체 취급: 할당 가능
def func1():
    print('func1 호출')
    
print(func1)
# 함수도 class의 형태이다
print(type(func1))

func2=func1
print(func2)
print(type(func2))

print(func1)
print(id(func2))