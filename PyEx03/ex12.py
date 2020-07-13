'''
Created on 2020. 7. 8.

@author: kim01
'''


def func(a, b):
    print(a, b)


# parameter를 할당 가능
a = 10
b = 20
func(a=100, b=200)


def func2(a, b, c=True):
    print(a, b, c)

    
a = 10
b = 20
c = False

func2(a, b, c)
func2(a, b) # c는 True
