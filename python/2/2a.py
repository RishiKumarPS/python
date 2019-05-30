class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(self, p):
        r = Point(self.x + p.x, self.y + p.y)
        return r
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
a=Point(1,2)
b=Point(2,3)
c=a+b
print('Point a:',a,'\nPoint b:',b,'\nPoint c=a+b:',c)
