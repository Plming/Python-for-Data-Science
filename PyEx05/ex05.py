'''
Created on 2020. 7. 10.

@author: kim01
'''
print('시작')

num1 = 10
num2 = 0

try:
    # ZeroDivisionError: division by zero
    print(num1 / num2)
except ZeroDivisionError as e:
    print('에러 발생:', e)

print('끝')
