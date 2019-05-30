from tkinter import *
def draw():
    c.create_oval(50,50,250,250,fill='green')
root=Tk()
c=Canvas(root,height=300,width=300)
b=Button(root,text="Draw Circle",command=draw).pack(side=BOTTOM)
c.pack()
root.mainloop()
