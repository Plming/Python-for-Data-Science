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
    
    # execute후, commit하고 close
    cursor = conn.cursor()
    
    # select 이외에는 전부 아래와 같은 방법으로 처리한다
    # sql_insert = ("insert into testtbl values('111','222')")
    data1 = '111'
    data2 = '222'
    sql_insert = ("insert into testtbl values('%s', '%s' )" % (data1, data2))
    cursor.execute(sql_insert)
    
    # sql_delete = ("delete from testtbl")
    # cursor.execute(sql_delete)
    
    print('실행완료')
    
    conn.commit()
    cursor.close()
    
except MySQLdb.Error as err:
    print('[에러]', err)

finally:
    conn.close()
