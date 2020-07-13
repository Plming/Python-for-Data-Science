'''
Created on 2020. 7. 9.

@author: kim01
'''


class FourCal:

    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def test(self):
        print('난 공유 객체')
        

# 상속(공유 - 파생)
class MoreFourCal(FourCal):

    def pow(self):
        result = self.first ** self.second
        return result
    
    # 오버라이드(재정의) - 부모 것을 버리고 재생성
    def test(self):
        print('난 파생 객체')


# 인스턴스화(인스턴스를 만드는 과정)
f = FourCal(10, 2)
print(f.add())

m = MoreFourCal(4, 2)
print(m.add())
print(m.sub())
print(m.pow())
m.test()
