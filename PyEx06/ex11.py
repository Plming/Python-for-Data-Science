'''
Created on 2020. 7. 11.

@author: kim01
'''
import pickle

# binary file 읽기
f=open('./test2.dat','rb')

data=pickle.load(f)
print(type(data))
print(data)

f.close()