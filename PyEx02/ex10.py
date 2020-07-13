'''
Created on 2020. 7. 7.

@author: kim01
'''
data = 10
print(data)

# 파이썬의 독특한 문법
(data1, data2) = ('Python', 'Life')
data1, data2 = ('Python', 'Life')
print(data1)
print(data2)

# 참고로 리스트도 이게 된다
[data3, data4] = ['Python', 'Life']
print(data3)
print(data4)

# 응용: 버블 정렬에서 값을 스왑
num1=10
num2=20
num1,num2=num2,num1
print(num1)
print(num2)