from re import *
s=input('Enter the string: ')
p='[aeiou]'
def exclamation(s):
    m=search(p,s,flags=IGNORECASE)
    if m:
        s = sub('a', 'aaaa', s, IGNORECASE)
        s = sub('e', 'eeee', s, IGNORECASE)
        s = sub('i', 'iiii', s, IGNORECASE)
        s = sub('o', 'oooo', s, IGNORECASE)
        s = sub('u', 'uuuu', s, IGNORECASE)
    s+='!'
    return s
s=exclamation(s)
print(s)
