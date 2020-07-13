'''
Created on 2020. 7. 8.

@author: kim01
'''
lists = [1, 2, 3]
for list in lists:
    print(list)
    
lists=['111', '222', '333']
for list in lists:
    print(list)
    
# string도 list처럼 in을 통해 된다.   
lists = 'Hello'
for list in lists:
    print(list)

#
lists=[(1, 2), (3, 4), (5, 6)]
for (first, last) in lists:
    print(first,':',last)