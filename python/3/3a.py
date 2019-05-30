class Vehicle:
    def __init__(self,cn):
        self.cn=cn
class Bike(Vehicle):
    def __init__(self,cn,n):
        Vehicle.__init__(self,cn)
        self.n=n
class Car(Vehicle):
    def __init__(self,cn,n,m):
        Vehicle.__init__(self,cn)
        self.n=n
        self.m = m
    def __str__(self):
        return ('Company Name: '+str(self.cn)+'\nCar name: '+str(self.n)+'\nMileage:'+str(self.m)+'kmpl')
class Pedal_bike(Bike):
    def __init__(self,cn,n,m):
        Bike.__init__(self,cn,n)
        self.m=m
    def __str__(self):
        return ('Company Name: '+str(self.cn)+'\nPedal Bike name:'+str(self.n)+'\nMileage: '+str(self.m)+'kmpl')
class Motor_bike(Bike):
    def __init__(self,cn,n,m):
        Bike.__init__(self,cn,n)
        self.m=m
    def __str__(self):
        return ('Company Name: '+str(self.cn)+'\nMotor Bike name:'+str(self.n)+'\nMileage: '+str(self.m)+'kmpl')
c=Car('BMW','i8',47)
p=Pedal_bike('P','p',100)
m=Motor_bike('M','m',90)
print('CAR:',c,'\nPEDAL BIKE',p,'\nMOTOR BIKE',m,sep='\n')
