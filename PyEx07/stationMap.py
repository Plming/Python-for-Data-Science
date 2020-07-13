'''
Created on 2020. 7. 13.

@author: kim01
'''
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import json
import webbrowser

strStation = input('역 이름 입력:')

url = 'https://maps.googleapis.com/maps/api/geocode/json?'
queryString = {
    'address':strStation,
    'language':'ko',
    'key':'AIzaSyAHw7XNNJpAr_CkboD9KmZpWm_nASVOdI4'
}

req = Request(url + urlencode(queryString))
urldata = urlopen(req)

jsonString = urldata.read().decode('utf-8')

jsonData = json.loads(jsonString)

lat = jsonData['results'][0]['geometry']['location']['lat']
lng = jsonData['results'][0]['geometry']['location']['lng']

webbrowser.open('https://www.google.com/maps/@%s,%s,16z' % (lat, lng))
