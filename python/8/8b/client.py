from Area import *
while(1):
    print()
    print('Area Menu'.center(19,'*'))
    c=int(input('1. Area of circle\n2. Area of rectangle\n3. Area of a triangle\n4. Exit\nEnter your choice: '))
    if c==1:
        r=float(input('Enter the radius of the circle: '))
        print('Area:',area_circle(r))
    elif c==2:
        print('Enter length and breadth of the rectangle: ',end='')
        s=[float(x) for x in input().split()]
        l=s[0]
        b=s[1]
        print('Area:',area_rectangle(l,b))
    elif c==3:
        print('Enter the sides of the triangle ', end='')
        s = [float(x) for x in input().split()]
        a = s[0]
        b = s[1]
        c = s[2]
        print('Area:', area_triangle(a,b,c))
    elif c==4:
        break
1
