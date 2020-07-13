'''
Created on 2020. 7. 8.

@author: kim01
'''
print('시작')

# global variable
a=1

def func(a):
    # local variable
    a=a+1
    print('a1:',a)

func(2)
print('a2:',a)
print('끝')