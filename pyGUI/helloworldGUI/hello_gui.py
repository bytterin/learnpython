# -*- coding: utf-8 -*-

'''
Created on 2016年4月12日

@author: Bytterin
'''

from Tkinter import *
import tkMessageBox

class Application(Frame):

    
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
        
    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hellow, %s' % name)
    
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
        
app = Application()
app.master.title('hello')
app.mainloop()
        
        