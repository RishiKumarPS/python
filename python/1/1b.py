from tkinter import *
def up():
    v.set(v.get()+1)
def down():
    v.set(v.get()-1)
if __name__=='__main__':
    root=Tk()
    v=IntVar()
    v.set(0)
f=Frame(root).pack()
b1=Button(f,text='UP',command=up).pack()
b2=Button(f,text='DOWN',command=down).pack()
l=Label(f,textvariable=v).pack(side=BOTTOM)
root.mainloop()
