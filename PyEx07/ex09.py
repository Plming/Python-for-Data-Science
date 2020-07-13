'''
Created on 2020. 7. 13.

@author: kim01
'''
from urllib.request import Request, urlopen
from urllib.parse import urlencode

url = 'https://maps.googleapis.com/maps/api/geocode/json?'
queryString = {'address':'안동대학교', 'language':'ko', 'key':'AIzaSyAHw7XNNJpAr_CkboD9KmZpWm_nASVOdI4'}

req = Request(url + urlencode(queryString))

urldata = urlopen(req)

html = urldata.read()
print(html.decode('utf-8'))

# 문자열 => json
# {'키':'값', '키':'값', ... } - 객체(dictionary)
# [] - 배열(리스트)
