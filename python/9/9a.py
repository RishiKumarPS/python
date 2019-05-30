class time:
    def __init__(self,h=0,m=0,s=0):
        self.hours=h
        self.minutes=m
        self.seconds=s
    def set_time(self,h,m,s):
        self.hours = h
        self.minutes = m
        self.seconds = s
    def __str__(self):
        return 'Time: '+str(self.hours)+':'+str(self.minutes)+':'+str(self.seconds)
    def get_seconds(self):
        return self.hours*3600+self.minutes*60+self.seconds
t=time()
h,m,s=input('Enter hours, minutes and seconds: ').split()
h=int(h)
m=int(m)
s=int(s)
t.set_time(h,m,s)
print(t,'has',t.get_seconds(),'seconds')
