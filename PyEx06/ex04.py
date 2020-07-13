'''
Created on 2020. 7. 11.

@author: kim01
'''

f = open('./test.txt', 'w')

# for i in range(1, 11):
#     data = '%d lines\n' % i
#     f.write(data)

data = ''
for i in range(1, 11):
    data = data + '%d lines.\n' % i
    
f.write(data)

f.close()
