#eg.Phone number: (800) 555.1212 #1234
from re import *
while(1):
    n,s=input('Enter a name and phone-number (eg, abcd : phonenumber): ').split(' : ')
    r=search(r'\(\d{3}\)\ \d{3}\.\d{4}\ \#\d{4}',s)
    if r:
        print('Validated correctly!')
        break
    else:
        print('Please enter a valid phone-number')
