'''
Created on 2020. 7. 11.

@author: kim01
'''

import pickle

# 바이너리 쓰기
f = open('test2.dat', 'wb')

data = {1:'python', 2:'java'}
pickle.dump(data, f)
print('출력 완료')

f.close()