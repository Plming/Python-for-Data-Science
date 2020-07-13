'''
Created on 2020. 7. 11.

@author: kim01
'''
import MySQLdb

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123456',
    'database': 'sample'
    }

conn = MySQLdb.connect(**config)
print(conn)

if conn:
    print('데이터베이스 연결 성공')

conn.close()
