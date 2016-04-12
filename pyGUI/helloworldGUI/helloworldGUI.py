# -*- coding: utf-8 -*-
'''
Created on 2016年4月12日
a sample of small python GUI
@author: Bytterin
'''

from Tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.helloLabel = Label(self, text = 'Hello, World!')
        self.helloLabel.pack()
        self.quitButon = Button(self, text = 'Quit', command=self.quit)
        self.quitButon.pack()
        

app = Application()
app.master.title("Hello World")
app.mainloop()
        