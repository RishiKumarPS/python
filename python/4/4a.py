try:
    l={}
    print('Accessing l[1] from l={}')
    q=l[1]
except KeyError:
    print('Key Error!')
try:
    a=1
    print('\na=1 and changing value to a=int("dog")')
    a=int('dog')
except ValueError:
    print('Value Error!')
try:
    p = [1, 2]
    print('\nAccessing p[3] from p=[1,2]')
    q=p[3]
except IndexError:
    print('Index Error!')
