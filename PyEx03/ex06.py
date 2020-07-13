'''
Created on 2020. 7. 8.

@author: kim01
'''
lists = [1, 2, 3, 4]
result = []
for list in lists:
    result.append(list * 3)

print(result)

# 숨겨진 for문 신기방기 - List comprehension
result = [list * 3 for list in lists]
print(result)

result = [list * 3 for list in lists if list % 2 == 0]
print(result)

result = [x * y
        for x in range(1, 10)
        for y in range(3, 6)
        ]
print(result)