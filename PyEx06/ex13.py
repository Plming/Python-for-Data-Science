'''
Created on 2020. 7. 11.

@author: kim01
'''
import tempfile

f=tempfile.mktemp()
print(f)
# C:\Users\kim01\AppData\Local\Temp\tmp2wqc6_b5

# close로 임시 파일 삭제
# 응용: 프로그램을 인스톨

f.close()