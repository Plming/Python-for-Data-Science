'''
Created on 2020. 7. 13.

@author: kim01
'''
from urllib.request import Request, urlopen
from urllib.parse import urlencode

url = 'https://search.naver.com/search.naver?'
queryString = {'query':'covid-19'}

req = Request(url + urlencode(queryString))

urldata = urlopen(req)

html=urldata.read()
print(html.decode('utf-8'))