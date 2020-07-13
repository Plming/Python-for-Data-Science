'''
Created on 2020. 7. 9.

@author: kim01
'''


class Cookie:

    def func1(self):
        # 동적으로 멤버필드를 선언할 수 있다.
        self.a = 10
        
    def func2(self):
        print(self.a)
 
c1 = Cookie()
c1.func1()
c1.func2()

print(c1.a)

c2=Cookie()
print(id(c1))
print(id(c2))

# 인스턴스의 멤버필드
c1.a=10
c2.a=20

# cf. 클래스의 멤버필드