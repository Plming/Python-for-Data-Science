'''
Created on 2020. 7. 8.

@author: kim01
'''
def subfunc():
    print('subfunc 호출됨')
    
def mainfunc(sub):
    # sub=subfunc
    sub()
    
mainfunc(subfunc)