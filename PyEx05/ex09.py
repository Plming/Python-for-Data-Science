'''
Created on 2020. 7. 10.

@author: kim01
'''


# 사용자 정의 exception, Exception을 상속받아 사용
class MyError(Exception):

    def __str__(self):
        return '에러발생 내용'


class Bird:

    def fly(self):
        # 강제 exception 발생
        raise MyError()    
        # if / try except => 대신 처리할 것을 위임
        
    
try:
    b = Bird()
    b.fly()
    print('정상 동작')
    
except MyError as e:
    print('예외 발생:', e)
