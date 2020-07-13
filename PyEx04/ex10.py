'''
Created on 2020. 7. 9.

@author: kim01
'''


class Family:
    # 초기화
    lastname = '김'

    
print(Family.lastname)

f1 = Family()
f2 = Family()

print(f1.lastname)
print(f2.lastname)

# 재선언
# f1.lastname='이얏호'
Family.lastname='박'

print(f1.lastname)
print(f2.lastname)
print(Family.lastname)

# 재선언이 되지 않는 한 lastname의 메모리 주소는 같으나..
print(id(f1.lastname))
print(id(f2.lastname))
print(id(Family.lastname))
print()

# f1, f2, Family의 주소는 모두 다르다
print(id(f1))
print(id(f2))
print(id(Family))