'''
Created on 2020. 7. 7.

@author: kim01
'''
# if도 중첩이 가능하다

# if 뒤에 없으면 에러남
# 따라서 pass를 넣음

money = True
car = False

print('시작')
if money:
    if car:
        print('A')
    else:
        print('B')
else:
    if car:
        print('C')
    else:
        print('D')
print('종료')
