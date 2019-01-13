'''
Created on 2018/11/23

@author: mog
'''
from tkinter import *
from tkinter import ttk
from abc import abstractmethod
from model.RedmineData import RedmineData

class RIddTab2():
    '''
    TableタブのRクラス
    '''

    def __init__(self, tab2):
        '''
        Constructor
        '''
        self.tab2 = tab2
        self.initTab2()

    def initTab2(self):
        """
        コントロールの設置
        """
        labelTicketNo = ttk.Label(self.tab2,text="TicketNo.",font=("游ゴシック",15))
        labelTime = ttk.Label(self.tab2, text = "工数", font=("游ゴシック", 15))
        labelActivity = ttk.Label(self.tab2,text="Activity",font=("游ゴシック",15))
        labelComment = ttk.Label(self.tab2,text="Comment",font=("游ゴシック",15))

        self.entryTicketNo1 = ttk.Entry(self.tab2, width = 8, font=("游ゴシック", 15))
        self.entryComment1 = ttk.Entry(self.tab2, width = 23, font=("游ゴシック", 15))
        self.entryTime1 = ttk.Entry(self.tab2, width = 5, font=("游ゴシック", 15))
        self.comboBoxActivity1 = ttk.Combobox(self.tab2, state = 'readonly', width = 15, font=("游ゴシック", 10))

        self.entryTicketNo2 = ttk.Entry(self.tab2, width = 8, font=("游ゴシック", 15))
        self.entryComment2 = ttk.Entry(self.tab2, width = 23, font=("游ゴシック", 15))
        self.entryTime2 = ttk.Entry(self.tab2, width = 5, font=("游ゴシック", 15))
        self.comboBoxActivity2 = ttk.Combobox(self.tab2, state = 'readonly', width = 15, font=("游ゴシック", 10))

        self.entryTicketNo3 = ttk.Entry(self.tab2, width = 8, font=("游ゴシック", 15))
        self.entryComment3 = ttk.Entry(self.tab2, width = 23, font=("游ゴシック", 15))
        self.entryTime3 = ttk.Entry(self.tab2, width = 5, font=("游ゴシック", 15))
        self.comboBoxActivity3 = ttk.Combobox(self.tab2, state = 'readonly', width = 15, font=("游ゴシック", 10))

        self.entryTicketNo4 = ttk.Entry(self.tab2, width = 8, font=("游ゴシック", 15))
        self.entryComment4 = ttk.Entry(self.tab2, width = 23, font=("游ゴシック", 15))
        self.entryTime4 = ttk.Entry(self.tab2, width = 5, font=("游ゴシック", 15))
        self.comboBoxActivity4 = ttk.Combobox(self.tab2, state = 'readonly', width = 15, font=("游ゴシック", 10))

        self.entryTicketNo5 = ttk.Entry(self.tab2, width = 8, font=("游ゴシック", 15))
        self.entryComment5 = ttk.Entry(self.tab2, width = 23, font=("游ゴシック", 15))
        self.entryTime5 = ttk.Entry(self.tab2, width = 5, font=("游ゴシック", 15))
        self.comboBoxActivity5 = ttk.Combobox(self.tab2, state = 'readonly', width = 15, font=("游ゴシック", 10))

        self.entryTicketNo6 = ttk.Entry(self.tab2, width = 8, font=("游ゴシック", 15))
        self.entryComment6 = ttk.Entry(self.tab2, width = 23, font=("游ゴシック", 15))
        self.entryTime6 = ttk.Entry(self.tab2, width = 5, font=("游ゴシック", 15))
        self.comboBoxActivity6 = ttk.Combobox(self.tab2, state = 'readonly', width = 15, font=("游ゴシック", 10))

        self.sendButton = ttk.Button(self.tab2, text = "send", width = 10)
        self.sendButton.bind('<Button-1>', self.actionExecute)

        labelTicketNo.grid(row=0, column = 0, padx = 5, pady = 5)
        labelActivity.grid(row=0, column = 1, padx = 5, pady = 5)
        labelTime.grid(row=0, column = 2, padx = 5, pady = 5)
        labelComment.grid(row=0, column = 3, padx = 5, pady = 5)

        self.entryTicketNo1.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.comboBoxActivity1.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.entryTime1.grid(row = 1, column = 2, padx = 5, pady = 5)
        self.entryComment1.grid(row = 1, column = 3, padx = 5, pady = 5)

        self.entryTicketNo2.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.comboBoxActivity2.grid(row = 2, column = 1, padx = 5, pady = 5)
        self.entryTime2.grid(row = 2, column = 2, padx = 5, pady = 5)
        self.entryComment2.grid(row = 2, column = 3, padx = 5, pady = 5)

        self.entryTicketNo3.grid(row = 3, column = 0, padx = 5, pady = 5)
        self.comboBoxActivity3.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.entryTime3.grid(row = 3, column = 2, padx = 5, pady = 5)
        self.entryComment3.grid(row = 3, column = 3, padx = 5, pady = 5)

        self.entryTicketNo4.grid(row = 4, column = 0, padx = 5, pady = 5)
        self.comboBoxActivity4.grid(row = 4, column = 1, padx = 5, pady = 5)
        self.entryTime4.grid(row = 4, column = 2, padx = 5, pady = 5)
        self.entryComment4.grid(row = 4, column = 3, padx = 5, pady = 5)

        self.entryTicketNo5.grid(row = 5, column = 0, padx = 5, pady = 5)
        self.comboBoxActivity5.grid(row = 5, column = 1, padx = 5, pady = 5)
        self.entryTime5.grid(row = 5, column = 2, padx = 5, pady = 5)
        self.entryComment5.grid(row = 5, column = 3, padx = 5, pady = 5)

        self.entryTicketNo6.grid(row = 6, column = 0, padx = 5, pady = 5)
        self.comboBoxActivity6.grid(row = 6, column = 1, padx = 5, pady = 5)
        self.entryTime6.grid(row = 6, column = 2, padx = 5, pady = 5)
        self.entryComment6.grid(row = 6, column = 3, padx = 5, pady = 5)

        self.sendButton.place(x = 240, y = 300)

        self.setActivity()
        self.redmineDataList = [[self.entryTicketNo1, self.comboBoxActivity1, self.entryTime1, self.entryComment1],
                                                [self.entryTicketNo2, self.comboBoxActivity2, self.entryTime2, self.entryComment2],
                                                [self.entryTicketNo3, self.comboBoxActivity3, self.entryTime3, self.entryComment3],
                                                [self.entryTicketNo4, self.comboBoxActivity4, self.entryTime4, self.entryComment4],
                                                [self.entryTicketNo5, self.comboBoxActivity5, self.entryTime5, self.entryComment5],
                                                [self.entryTicketNo6, self.comboBoxActivity6, self.entryTime6, self.entryComment6]]

    def setActivity(self):
        activityList = [self.comboBoxActivity1, self.comboBoxActivity2, self.comboBoxActivity3, self.comboBoxActivity4,
                        self.comboBoxActivity5, self.comboBoxActivity6]

        activityTaple = RedmineData.getActivityTaple()

        for comboBox in activityList:
            comboBox["values"] = activityTaple


    @abstractmethod
    def actionExecute(self, event):
        pass

    @abstractmethod
    def initializeCreation(self):
        pass
