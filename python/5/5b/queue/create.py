class Queue:
    def __init__(self,l=[]):
        self.l=l
    def insert(self,x):
        self.l.append(x)
    def front(self):
        return self.l[0]
    def rear(self):
        return self.l[-1]
    def remove(self):
        self.l.pop(0)
    def __str__(self):
        return str(self.l)
