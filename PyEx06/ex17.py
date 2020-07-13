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

try:
    conn = MySQLdb.connect(**config)
    print('데이터베이스 연결 성공')
    
    cursor = conn.cursor()
    sql_select = ('select col1, col2 from testtbl')
    cursor.execute(sql_select)
    
    for (col1, col2) in cursor:
        print(col1, col2)
    
    cursor.close()
    
    print('실행 완료')
    
except MySQLdb.Error as err:
    print('[에러]', err)

finally:
    conn.close()
