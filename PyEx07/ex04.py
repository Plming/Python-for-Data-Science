'''
Created on 2020. 7. 13.

@author: kim01
'''
from urllib.parse import urlparse

strurl = 'https://search.naver.com:8080/search.naver?sm=top_sug.pre&fbm=0&acr=1&acq=covid&qdt=0&ie=utf8&query=covid-19'
url = urlparse(strurl)

print('url:', url)
print('scheme:', url.scheme)
print('host:', url.hostname)
print('port:', url.port)
print('path:', url.path)
print('query:', url.query)

'''
요청 url
프로토콜
https
://
도메인(ip)
search.naver.com
/
요청 경로
search.naver
?
질의어
키=값
sm=top_sug.pre
&
fbm=0
&
acr=1
&
acq=covid
&
qdt=0
&
ie=utf8
&
query=covid-19
'''

