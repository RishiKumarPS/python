from tkinter import *
def second():
    l=Label(root,text='Nice Job!',fg='green').pack()
def first():
    b2=Button(root,text='Second',command=second).pack()
root=Tk()
b1=Button(root,text='First',command=first).pack()
root.mainloop()
