'''
Created on 2020. 7. 13.

@author: kim01
'''
import MySQLdb

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123456',
    'database':'sample',
    'charset':'utf8'
}

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    
    inputData = input('동 이름 입력:')
    
    sql_select = ("select zipcode, sido, gugun, dong, ri, bunji from zipcode where dong like '%s%%'" % inputData)
    cursor.execute(sql_select)
        
    for (zipcode, sido, gugun, dong, ri, bunji) in cursor:
        print('[', zipcode, ']', sido, gugun, dong, ri, bunji)
    
    cursor.close()
    
except MySQLdb.Error as err:
    print('에러', err)
    
finally:
    conn.close()