'''
Created on 2020. 7. 6.

@author: kim01
'''
print(' I eat five apples')
print(' I eat %s apples' % 'five')

data = 'six'
print(' I eat %s apples' %data)

unit = 'pears'
print(' I eat %s %s'%(data, unit))

str = ' I eat %s %s'%(data, unit)
print(str)

# format function
print('I eat {0} apples'.format('five'))
print('I eat {0} {1}'.format(data, unit))