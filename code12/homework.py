# -*- coding=utf-8 -*-

from Tkinter import *

class myButton:
    def __init__(self):
        self.__mainwn = Tk()
        self.strtext = "Welcome to GUI programming"
        self.label = Label(self.__mainwn,text=self.strtext)
        self.btOK = Button(self.__mainwn,text="OK",command=self.processOK)
        self.btCancel = Button(self.__mainwn, text="Cancel", command=self.processCancal)
        self.label.pack()
        self.btOK.pack()
        self.btCancel.pack()
        self.__mainwn.mainloop()

    def processOK(self):
        self.label['text'] = 'OK is clicked'


    def processCancal(self):
        self.label['text'] = 'Cancel is clicked'

bt = myButton()
