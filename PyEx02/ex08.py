'''
Created on 2020. 7. 7.

@author: kim01
'''
# dictionary
# list: 인덱스(숫자)
# dict: 문자열(사전)
# 단어(key) -> 내용(value)

dict = {
    'name': 'pey',
    'phone': '011111111222',
    'birth': [11, 18]
}
print(dict)
print(type(dict))

# 인덱싱=> key
print(dict['name'])

# 추가 (키가 없으면 추가) / 수정(키가 있으면 수정)
dict['age'] = 20
print(dict)

dict['age'] = 40
print(dict)

# 삭제
del dict['age']
print(dict)

# key 목록
print(dict)
keys = dict.keys()
# list와 비슷한 구조 dict_keys
print(keys)
print(type(keys))
# 그럼 list로 만들자
list = list(keys)
print(list)

# value 목록
values = dict.values()
print(values)
print(type(values))

# key, value 다 가져오기
items = dict.items()
print(items)
print(type(items))

# 데이터 지우기
# dict.clear()
print(dict)

# 키를 검사하는 구문
print(dict)
print('name' in dict)
print('email' in dict)
