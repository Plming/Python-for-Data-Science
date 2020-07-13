'''
Created on 2020. 7. 7.

@author: kim01
'''
# 집합 자료형
set1 = set()
print(type(set1))

set2 = set([1, 2, 3, 4, 5, 6, 4, 5, 6])
print(type(set2))
print(set2)

set3 = set('hello world')
print(set3)

# 
list = list(set2)
print(list)
print(list[2])

# 집합 연산: 교집합, 합집합, 차집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1)
print(s2)

# 교집합
print(s1 & s2)
print(s1.intersection(s2))
# 합집합
print(s1 | s2)
print(s1.union(s2))
# 차집합
print(s1 - s2)
print(s1.difference(s2))

# data 추가
print(set2)
set2.add(10)
set2.add(4)
print(set2)

# 여러 개 값 추가
set2.update([10, 20, 30])
print(set2)

# 값 제거
set2.remove(10)
print(set2)

# 