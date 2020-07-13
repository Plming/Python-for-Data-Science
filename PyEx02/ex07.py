'''
Created on 2020. 7. 7.

@author: kim01
'''
list1 = [1, 2, 3]
print(list1)

# 값을 전달하는 게 아닌, 레퍼런스를 전달 (shadow copy)
# 저장 메모리(공통 사용)
list2 = list1
print(list1)
print(list2)

list1[0] = 10
print(list1)
print(list2)

print(id(list1))
print(id(list2))

# 값을 복사하는 방법(deep copy) - 슬라이싱 사용
# 혹은 copy() 사용
list3 = list1[:]
print(list1)
print(list3)
print(id(list1))
print(id(list3))
list1[0] = 100
print(list1)
print(list3)
