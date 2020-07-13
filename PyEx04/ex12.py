'''
Created on 2020. 7. 9.

@author: kim01
'''


class FourCal:

    def __init__(self, first, second):
        print('init 호출')
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result

     
f = FourCal(10, 20)
print(f.add())
