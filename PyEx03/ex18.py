'''
Created on 2020. 7. 8.

@author: kim01
'''
# help(print)

# all - list의 모든 data가 참일 때 참
# any - list의 하나 이상의 data가 참일 때 참
print(all([1, 2, 0]))
print(any([0, 0, 0]))

# enumerate형으로 변환
lists = ['body', 'foo', 'bar']
for i, name in enumerate(lists):
    print(i, name)
    
# 문자열을 실행문으로 바꿔줌 eval
str = '1+2'
print(str)
print(eval(str))

# len

# 각종 자료형 변환 함수
# 자료형()
# int(), str(), list()

# 수학 관련
print(abs(-123))

print(7 // 3)
print(7 % 3)
# (몫, 나머지) tuple 형태로 반환
print(divmod(7,3))

# 최댓값 찾기, str도 가능하다
print(max([1,2,3]))
print(max('python'))

# pow/round
print(sum([1,2,3]))
print(sum(range(0,101,2)))