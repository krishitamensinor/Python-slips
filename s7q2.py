from tkinter import *
w=Tk()
lb=Listbox(w)
lb.insert(1,"Python")
lb.insert(2,"Java")
lb.insert(3,"C")

lb.pack()
w.mainloop()