def sublist(a,b):
    ind=0
    for i in a:
        if i not in b[ind:]:
            return False
        else:
            ind=b.index(i)
    return True
print('Enter list 1 elements: ',end='')
l1=[int(x) for x in input().split()]
print('Enter list 2 elements: ',end='')
l2=[int(x) for x in input().split()]
print(sublist(l1,l2))
