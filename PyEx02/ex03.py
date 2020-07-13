'''
Created on 2020. 7. 7.

@author: kim01
'''

# [] / list()
list1=[]
list2=list()

print(type(list1))
print(type(list2))

list3=[1,3,5,7,9]
print(list3)

list4 = ['1','3','5','7','9']
print(list4)

# 한 가지 자료형을 넣고 활용하는 것이 좋음
list5=[1,3,'111','333']
print(list5)

# 문자열과 동일하게 인덱싱을 통해 list의 원소에 접근
# 0부터 센다
print(list3[0])
print(list3[2])

# 범위를 벗어날 경우 에러 out of range
# print(list3[10])

print(list3[-1])