# -*- coding=utf-8 -*-

from Tkinter import *

def processOK():
    print u"Ok按钮被点击"
    label['text'] = "Ok"

def processCancal():
    print u"Cancal按钮被点击"
    label['text'] = "Cancel"

window = Tk()
label = Label(window,text="Welcome to GUI programming")
btOK = Button(window,text="OK",fg="red",command=processOK)
btCancel = Button(window,text="Cancel",bg="lightblue",command=processCancal)

label.pack()
btOK.pack()
btCancel.pack()

window.mainloop()