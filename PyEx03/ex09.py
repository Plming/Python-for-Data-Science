'''
Created on 2020. 7. 8.

@author: kim01
'''


# 선언
def func1():
    pass


def func2():
    a = 10
    print('func2 호출:', a)


def func3(a):
    print('func3 호출:', a)


def func4(a, b, c):
    print('func4호출:', a)
    print('func4호출:', b)
    print('func4호출:', c)


# return을 받도록
def func5(a, b):
    sum = a + b
    print(id(sum))
    return sum


result = func5(10, 20)
print(id(result))

result=len('hello')
print(result)
