'''
Created on 2020. 7. 8.

@author: kim01
'''

# range() - 숫자의 범위
print(list(range(5)))
print(list(range(5, 10)))

for i in range(0, 5):
    print(i)

# 1 ~ 10
for i in range(1, 11):
    print(i, end=' ')

print()

print(sum(range(11)))

sumVal = 0
for i in range(10):
    sumVal += i + 1
print(sumVal)