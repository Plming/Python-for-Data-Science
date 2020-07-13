'''
Created on 2020. 7. 9.

@author: kim01
'''


class Cookie:
    # 클래스 변수
    a = 10
    b = 10

    
c1 = Cookie()
print(id(c1))

# .: 객체 참조 연산자
c1.a = 100
c1.b = 200

print(c1.a)
print(c1.b)
print(Cookie.a)