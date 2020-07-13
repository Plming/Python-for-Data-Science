'''
Created on 2020. 7. 9.

@author: kim01
'''


class FourCal:
    
    # setter 메소드
    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    # getter 메소드
    def getdata(self):
        return self.first, self.second


a = FourCal()
a.setdata(4, 2)
print(a.first, a.second)

result = a.getdata()
print(result)
