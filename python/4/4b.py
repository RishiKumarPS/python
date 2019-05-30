class Mylist:
    def __init__(self,l=[]):
        self.l=l
    def __add__(self,a):
        self.l.append(a)
        return self.l
    def __str__(self):
        return self.l
l=Mylist([1,2])
print('Adding 3 to the list [1, 2]')
l+=3
print('Updated list:',l)
