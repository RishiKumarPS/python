d={}
def new(w,m):
    d[w]=m
def retrieve(w):
    if w not in d:
        return -1
    return d[w]
def same_meaning(m):
    l=[]
    for i,j in d.items():
        if j==m:
            l.append(i)
        if len(l)==0:
            return -1
    return l
def remove(w):
    if w not in d:
        return -1
    d.pop(w)
    return 1
def display_sorted():
    print("DICTIONARY:")
    for i in sorted(d.keys()):
        print(i,':',d[i])
while(1):
    print()
    print('DICTIONARY MENU'.center(25,'*'))
    c=int(input('1. New Entry\n2. Retrieve meaning for a word\n3. Words with same meaning\n4. Remove an entry\n5. Display the dictionary\n6. Exit\nEnter your choice: '))
    if c==1:
        w,m=input('Enter word and its meaning (eg., word : meaning): ').split(' : ')
        new(w,m)
        print('New entry added!')
    elif c==2:
        w=input('Enter the word: ')
        k=retrieve(w)
        if k==-1:
            print('No such word in the dictionary')
        else:
            print('Meaning:',k)
    elif c==3:
        m=input('Enter the meaning: ')
        k=same_meaning(m)
        if k==-1:
            print('No words in the dictionary mean that!')
        else:
            for i in k:
                print(i,end=' ')
            print('(is/are) the word(s) that mean it')
    elif c==4:
        w=input('Enter the word to be removed: ')
        k=remove(w)
        if k==-1:
            print('No such word in the dictionary to be removed!')
        else:
            print(w,'is removed from the dictionary')
    elif c==5:
        display_sorted()
    elif c==6:
        break
