from Tkinter import *
root = Tk()
v = IntVar()

def getValue():
    print v.get()

Label(root,text="Choose a programming language",justify=LEFT,padx=20).pack()
Radiobutton(root,text="Python",padx=20,variable=v,value=1,command=getValue).pack(anchor=W)
Radiobutton(root,text="Javc",padx=20,variable=v,value=2,command=getValue).pack(anchor=W)

mainloop()