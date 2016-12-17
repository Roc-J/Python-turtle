from Tkinter import *

root = Tk()
v = IntVar()
v.set(1)

language = [("Python",1),("Perl",2),("Java",3),("C++",4),("C",5)]

def ShowChoice():
    print v.get()

Label(root,text="Choose your favourite programming language:",justify=LEFT,padx=20).pack()

for txt,val in language:
    Radiobutton(root,text=txt,padx=20,variable=v,command=ShowChoice,val=val).pack(anchor=W)

mainloop()