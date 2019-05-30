f=open('graffit.txt','r')
l=[]
for i in f.readlines():
    l.append(i.upper())
f.close()
f=open('graffit.txt','w')
for i in l:
    f.write(i)
f.close()
