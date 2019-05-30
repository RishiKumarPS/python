from re import *
def correct(s):
    s=sub(r'\ +',r' ',s)
    s=sub(r'\.',r'. ',s)
    return s
s=input('Enter the string: ')
print(correct(s))
