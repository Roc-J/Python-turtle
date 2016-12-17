from Tkinter import *
wn = Tk()

def var_status():
    print("male:%d,\n female:%d" % (var1.get(),var2.get()))

Label(wn,text="your sex:").grid(row=0,sticky=W)
var1 = IntVar()
Checkbutton(wn,text="male",variable=var1).grid(row=1,sticky=W)
var2 = IntVar()
Checkbutton(wn,text="female",variable=var2).grid(row=2,sticky=W)
Button(wn,text="Quit",command=wn.quit).grid(row=3,sticky=W,pady=4)
Button(wn,text="Show",command=var_status).grid(row=4,sticky=W,pady=4)

mainloop()