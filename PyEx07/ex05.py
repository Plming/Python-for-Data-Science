'''
Created on 2020. 7. 13.

@author: kim01
'''
from urllib.parse import urlunparse

# parse = 분해
# unparse는 url을 str로 반환
url = urlunparse(('http', 'www.exam.com', '/hello/test.py', '', '', ''))
print(url)
