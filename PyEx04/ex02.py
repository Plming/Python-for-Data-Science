'''
Created on 2020. 7. 9.

@author: kim01
'''


def two_times1(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result


result = two_times1([1, 2, 3, 4])
print(result)

def two_times2(x):
    return x*2

# 일급함수를 응용한 map 함수
result=map(two_times2,[1,2,3,4])
print(result)
print(list(result))

# lambda 헷갈려유
result=map(lambda x: x*2,[1,2,3,4])
print(list(result))