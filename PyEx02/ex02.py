'''
Created on 2020. 7. 7.

@author: kim01
'''
from gevent import __abstract_linkable

# str의 길이
str = 'Python is the best choice'

# function
print(len(str))

# . : 객체 참조연산자
# 클래스 안의 메서드나 멤버 필드 참조
# 특정 문자의 갯수
print(str.count('i'))

# 검색
print(str.find('b'))
# 없을 경우 -1 리턴
print(str.find('z'))

# 비슷한 메서드
print(str.index('b'))
# 없을 경우 에러 발생
# print(str.index('z'))

str2 = 'hi'
print(str2.upper())
str2 = 'HI'
print(str2.lower())

# 공백
str3 = '   hi   '
print(':'+str3.lstrip()+':')
print(':'+str3.rstrip()+':')
print(':'+str3.strip()+':')

# 치환
print(str)
print(str.replace('is', 'are'))