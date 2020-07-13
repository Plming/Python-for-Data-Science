'''
Created on 2020. 7. 7.

@author: kim01
'''
# tuple:
# list와 비슷하지만 수정이 안된다(read only)

tuple1 = ()
tuple2 = tuple()

print(type(tuple1))
print(type(tuple2))

tuple3 = (1, 2, 3)
print(tuple3)

# 1개짜리 튜플은 없다.
# tuple4 = (1) 이건 int다
tuple4 = (1,)
print(tuple4)
print(type(tuple4))

# 이런 표기도 가능
tuple5 = 1, 2, 3
print(tuple5)

# 중첩 tuple
tuple6 = (1, 2, 3, (4, 5))
print(tuple6)

# 인덱싱
print(tuple3)
print(tuple3[0])

# 삭제/수정은 안된다
# del tuple3[0]
# tuple3[0]=3
