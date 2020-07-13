'''
Created on 2020. 7. 7.

@author: kim01
'''

# slicing
list = [1, 2, 3, 4, 5]
print(list[0:2])
print(list[2:])
print(list[:2])

list2 = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(list2[2:5])

# 중첩된 경우 별도로 인덱스를 지정
print(list2[3][:2])

# 리스트 연산: +, *
list3 = [1, 2, 3]
list4 = [4, 5, 6]
print(list3 + list4)
print(list3 * 3)

# 삭제도 된다
# del list[1]

# slicing으로 삭제도 가능
del list[2:]
print(list)