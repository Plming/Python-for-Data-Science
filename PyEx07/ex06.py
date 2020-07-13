'''
Created on 2020. 7. 13.

@author: kim01
'''
from urllib.parse import urlencode

form = {'name':'홍길동', 'phone':'010-1111-2222'}
encform = urlencode(form)

print(encform)
