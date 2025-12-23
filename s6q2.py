from tkinter import *

def hello():
  l.config(text="Hello User")
  
w=Tk()
e=Entry(w)
e.pack()

Button(w,text="hello",command=hello).pack()
Button(w,text="Exit",command=w.destroy).pack()

l=Label(w)
l.pack()
w.mainloop()