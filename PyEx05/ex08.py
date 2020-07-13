'''
Created on 2020. 7. 10.

@author: kim01
'''
print('시작')

i = 1
num1 = 10
num2 = 0

try:
    a = [1, 2]
    print(a[i])
    print(num1 / num2)
    
except (IndexError, ZeroDivisionError) as e:
    print('에러 발생:', e)

finally:
    # 무조건 동작
    # 정상 / 에러이든 무조건 실행하고 싶은 구문
    print('우헤헤헤헤헿ㅎㅎㅎㅎ')

print('끝')
