from math import *
def area_circle(r):
    return 4*atan(1)*(r**2)
def area_rectangle(l,b):
    return l*b
def area_triangle(a,b,c):
    s=(a+b+c)/2
    return sqrt(s*(s-a)*(s-b)*(s-c))
