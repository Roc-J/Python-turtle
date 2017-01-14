from Tkinter import *

window = Tk()
menubar = Menu(window)

filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Close")

menubar.add_cascade(label="File",menu=filemenu)

window.config(menu=menubar)
window.mainloop()