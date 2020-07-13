'''
Created on 2020. 7. 13.

@author: kim01
'''
from urllib.request import urlopen

# 객체 생성
urldata = urlopen('https://m.naver.com')
# print(urldata)

# print(urldata.headers)

# bytes
html = urldata.read()
print(html.decode('utf-8'))

# decode 후 str로 변환
strHtml=html.decode('utf-8')
print(type(strHtml))