'''
Created on 2020. 7. 8.

@author: kim01
'''

# marks(점수) 60이상 이면 합격/불합격
marks = [90, 25, 67, 45, 80]

for data in marks:
    if data >= 60:
        print('합격')
    else:
        print('불합격')

# 읽는 순서
index = 0
for mark in marks:
    index = index + 1
    if mark >= 60:
        print('%d번 학생은 합격' % index)
    else:
        print('%d번 학생은 불합격' % index)
