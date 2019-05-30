class Stack:
    def __init__(self,l=[]):
        self.l=l
    def insert(self,x):
        self.l.append(x)
    def top(self):
        return self.l[-1]
    def remove(self):
        self.l.pop()
    def __str__(self):
        return str(self.l)
