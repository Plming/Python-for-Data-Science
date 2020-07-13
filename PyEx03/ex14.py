'''
Created on 2020. 7. 8.

@author: kim01
'''

def func1(a,b):
    return a+b

result=func1(10,20)
print(result)

def func2(a,b):
    # 여러개 리턴도 가능
    # 이건 tuple로 리턴됨
    return a+b,a-b,a*b

result=func2(10,5)
print(type(result))
print(result[0])