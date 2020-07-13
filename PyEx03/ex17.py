'''
Created on 2020. 7. 8.

@author: kim01
'''


# lambda로 함수 만들기
def func11(a):
    return a


print('result:', func11(1))

func12 = lambda a : a + 10
print('result:', func12(1))
print(type(func12))


def func21(a, b):
    return a + b


print('result:', func21(10, 20))

func22 = lambda a, b:a + b

print('result:', func22(10, 20))
