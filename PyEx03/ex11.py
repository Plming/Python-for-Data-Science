'''
Created on 2020. 7. 8.

@author: kim01
'''
print('시작')

# global variable
a=1

def func():
    # global 변수를 참조할때는 global 키워드 사용
    global a
    # local variable
    a=a+1
    print('a1:',a)
    
func()
print('a2:',a)
print('끝')