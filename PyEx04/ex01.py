'''
Created on 2020. 7. 9.

@author: kim01
'''


# 고정인자는 가변인자 앞에
def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for arg in args:
            result = result + arg
            
    elif choice == 'mul':
        result = 1
        for arg in args:
            result = result * arg
            
    return result


print(add_mul('add', 2, 3, 4, 5))
