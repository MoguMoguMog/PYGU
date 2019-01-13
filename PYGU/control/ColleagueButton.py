'''
Created on 2018/11/04

@author: mog
'''
from tkinter import *
from tkinter import ttk

class ColleagueButton(ttk.Button):
    '''
    classdocs
    '''


    def __init__(self, label, tab, mediator):
        '''
        Constructor
        '''
        self.mediator = mediator
        super().__init__(tab, text = label, width = 10, command = self.stateChanged)

    def setMediator(self, mediator):
        self.mediator = mediator

    def stateChanged(self):
        self.mediator.colleagueChanged()
