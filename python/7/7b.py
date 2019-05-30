def remove(l,r): #for unique elements of x, y and z in list
    k=[]
    k+=l
    if r in l:
        k.remove(r)
    return k
def subsetsum(l,tar):
    k=[(x,y,z) for x in l for y in remove(l,x) for z in remove(remove(l,x),y) if x+y+z==tar]
    if len(k):
        return True
    return False
print('Enter the list elements: ',end='')
lst=[int(x) for x in input().split()]
t=int(input('Enter the target: '))
print(subsetsum(lst,t))
