'''
Created on 2020. 7. 8.

@author: kim01
'''
# 가변인자(인자 갯수를 정하지 않음)
# tuple이다

def func1(*args):
    print(type(args))
    print(args)
    
    for arg in args:
        print(arg,end='  ')
        

func1(1,2,3,4,5)