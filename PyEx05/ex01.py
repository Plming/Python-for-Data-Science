'''
Created on 2020. 7. 10.

@author: kim01
'''


class FourCal:

    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    # 내부적인 데이터를 표현, f로 참조    
    def __str__(self):
        return str(self.first) + ':' + str(self.second)
           
    def add(self):
        result = self.first + self.second
        return result


# 상속
class MoreFourCal(FourCal):
    pass

    
# 인스턴스화(변수)
m = MoreFourCal(10, 20)
print(m)
print(m.add())
