'''
Created on 2020. 7. 11.

@author: kim01
'''
import MySQLdb

file = open('./zipcode_all_utf8_type2.csv', 'r', encoding='utf-8')

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123456',
    'database': 'sample',
    'charset':'utf8'
    }

try:
    conn = MySQLdb.connect(**config)
    print('데이터베이스 연결 성공')
    
    cursor = conn.cursor()

    while True:
        line = file.readline()
        
        if not line:
            break
        
        # Data Example: 363-921,충북,청원군,북이면,서당리,,52095
        data = line.split(sep=',')
        data[6] = data[6].rstrip('\n')
        sql_insert = ("insert into zipcode values('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
        print('.', end='')
        cursor.execute(sql_insert)
        
    conn.commit()
    print('실행 완료')
    
except MySQLdb.Error as err:
    print('[에러]', err)

finally:
    cursor.close()
    conn.close()
    file.close()
