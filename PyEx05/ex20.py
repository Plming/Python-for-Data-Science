'''
Created on 2020. 7. 10.

@author: kim01
'''

import random

# 0 <= x < 1 무작위 수
print(random.random())

# 0 <= x < 10 정수
print(random.randint(0, 10))

# 1 <= x <= 45 정수
print(random.randint(1, 45))

# 로또 번호 추출기
# 중복을 허용 안함 => set
