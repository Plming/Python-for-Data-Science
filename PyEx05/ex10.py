'''
Created on 2020. 7. 10.

@author: kim01
'''
# command line 인수 참조 방법
import sys
# System-specific parameters and functions

# print(dir(sys))
# print(sys.argv)

# sys.argv는 리스트의 형태이다
argv=sys.argv

print(argv[0])
print(argv[1])
print(argv[2])
print(argv[3])