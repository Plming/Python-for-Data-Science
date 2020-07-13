'''
Created on 2020. 7. 13.

@author: kim01
'''
import json

# file = open('./geo.json', encoding='utf-8')
# data = json.loads(file)

with open('./geo.json', encoding='utf-8') as f:
    data = json.load(f)
    
    # json -> string 계열
    print('위도:', data['results'][0]['geometry']['location']['lat'])
    print('경도:', data['results'][0]['geometry']['location']['lng'])
