'''
Created on 2020. 7. 9.

@author: kim01
'''
class Cookie:
    
    # 메서드의 선언
    # self가 있어야 함
    def func1(self):
        print('func1 호출',self)
        
    def func2(self,a,b):
        print('func2 호출',a)
        print('func2 호출',b)
        
c1=Cookie()
c1.func1()
c1.func2(10,20)
