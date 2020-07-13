'''
Created on 2020. 7. 10.

@author: kim01
'''
print('시작')

i = 3
num1 = 10
num2 = 2

try:
    a = [1, 2]
    # IndexError: list index out of range
    print(a[i])
    # ZeroDivisionError: division by zero
    print(num1 / num2)
    
except IndexError as e:
    print('에러 발생:', e)

except ZeroDivisionError as e:
    print('에러 발생:', e)

print('끝')
