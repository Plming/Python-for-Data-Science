'''
Created on 2020. 7. 13.

@author: kim01
'''
import json

str1 = '{"name":"홍길동", "birth":"0530", "age":"30"}'

j1=json.loads(str1)
print(j1)
print(type(j1))

print(j1['name'])


str2 = '{"name":"홍길동", "birth":["10","20","30","40"], "age":"30"}'
j2=json.loads(str2)
print(j2['birth'][0])