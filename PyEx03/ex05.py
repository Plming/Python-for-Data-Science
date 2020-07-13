'''
Created on 2020. 7. 8.

@author: kim01
'''
# 중첩 for

for i in range(0, 3):
    for j in range(0, 3):
        print(i, ':', j, end='  ')
    print()

# list를 range를 통해 접근하자    
marks = [90, 25, 67, 45, 80]
for i in range(len(marks)):
    print(marks[i])
    
marks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(marks[0][0])
print(marks[0][2])

# 전체 데이터에 접근 - 2중 for
for i in range(len(marks)):
    for j in range(len(marks[i])):
        print(marks[i][j], end=' ')
    print()
    
