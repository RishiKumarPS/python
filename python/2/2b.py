def geometric(l):
    f=0
    r=l[1]/l[0]
    for i in range(2,len(l)):
        if (l[i]/l[i-1])!=r:
            f=1
            break
    if f:
        return False
    return True
print('Enter the list of numbers:')
p=[int(x) for x in input().split()]
print(geometric(p))
