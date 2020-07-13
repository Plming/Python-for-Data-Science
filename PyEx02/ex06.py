'''
Created on 2020. 7. 7.

@author: kim01
'''
# 요소 추가
# 단일 값 추가
list = [1, 2, 3]
list.append(4)
print(list)

# 리스트 추가
list.append([5, 6])
print(list)

list = [1, 4, 3, 2, 5, 8]
list.sort()
print(list)

# 문자 리스트도 사전식으로 정렬
# 코드값으로 정렬
slist = ['b', 'a', 'd', 'c']
slist.sort()
print(slist)

# 정렬 후 리버스 <=> 오름차순과 내림차순이 바뀜
slist.reverse()
print(slist)

# 검색, 없으면 에러 발생
print(list)
print(list.index(3))
print(list.index(1))
# print(list.index(0))

# 삽입
print(list)
list.insert(0, 4)
print(list)

# del 위치/ remove(값)
list.remove(3)
print(list)
# 같은 데이터 동시 삭제 되지 않음(여러번 수행)
list.remove(4)
print(list)

# 확장 +연산자와 비슷
print(list)
list.extend([4, 5])
print(list)

# 리스트와 문자열 ..
str = 'Hello Python 안녕 '
data = str.split()
print(data)
print(type(data))
print(data[0])

# 구분자 먼저 쓰고 join 메소드 참조하여 데이터를 연결
data2 = ','.join(data)
print(data2)
print(type(data2))

# split에 구분자(sep)를 지정할 수 있다
str = 'Hello,Python,안녕 '
data = str.split(',')
print(data)
print(type(data))
print(data[0])
