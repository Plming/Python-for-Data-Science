'''
Created on 2020. 7. 11.

@author: kim01
'''
import MySQLdb

# 127.0.0.1 / localhost - 내 컴퓨터
conn = MySQLdb.connect(host='127.0.0.1', user='root', password='123456', database='sample')
print(conn)

conn.close()