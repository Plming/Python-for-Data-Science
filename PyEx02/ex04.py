'''
Created on 2020. 7. 7.

@author: kim01
'''

# 중첩 리스트
# 리스트 안의 리스트
list = [1, 2, 3, ['a','b','c'] ]

print(list)
print(list[0])
print(list[3])

# n-ary array와 접근이 유사
print(list[3][0])
print(list[3][2])

# 원소 값의 변경 가능
list[0]=10
print(list)