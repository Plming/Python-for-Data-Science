'''
Created on 2020. 7. 11.

@author: kim01
'''

# 파일이 존재하면 쓰기모드로 열고,
# 파일이 존재하지 않으면 생성후 쓰기 모드로 연다
# overwrite(새로 성성후 씀)
f = open('./test.txt', 'w')
print(f)

# \n - 엔터
# \t - 탭
f.write('hello1\n')
f.write('hello1\n')
f.write('hello1\n')

# 열면 반드시 닫아야 함 (내용이 손상되지 않음)
f.close()