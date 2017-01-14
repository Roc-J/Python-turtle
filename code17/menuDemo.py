from Tkinter import *

class MenuDemo():
    def __init__(self):
        window = Tk()
        menubar = Menu(window)
        filemenu = Menu(menubar,tearoff=0)
        filemenu.add_command(label="New")
        window.config(menu=menubar)

        mainloop()

MenuDemo()