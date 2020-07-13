'''
Created on 2020. 7. 6.

@author: kim01
'''
str='Life is too short, You need Python'
print(len(str))

# 인덱싱(음수도 에러가 없다)
print( str[0] )
print( str[1] )
print( str[-1] )
print( str[-2] )

#슬라이싱
print( str[0:5] )
print( str[5:] )
print( str[:] )
print( str[:7])

# example
data='20201007Rainy'
year=data[:4]
day=data[4:8]
weather=data[8:]
print(year,day,weather)

str = 'Hello'
print(str[0])
# 읽기 전용
# 에러 발생!! str[0]='h'
str2='h'+str[1:]
print(str2)