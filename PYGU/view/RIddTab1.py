'''
Created on 2018/10/27

@author: mog
'''
from tkinter import *
from tkinter import ttk
from abc import  abstractmethod

from model.CircularProgressBar import CircularProgressBar
from control.ColleagueButton import ColleagueButton
from interface.IMediator import IMediator
from model.RedmineData import RedmineData
from redminelib import Redmine



class RIddTab1(IMediator):
    '''
    TimerタブのRクラス
    '''


    def __init__(self, tab1):
        """
        コンストラクタ
        """
        self.tab1 = tab1
        self.initTab1()
        self.createColleagues()
        pass


    def initTab1(self):
        """
        タイマータブのコントロール設置
        """
        self.ticketNo = StringVar()
        self.ticketNo.trace('w', self.executeEntry)
        self.comment = StringVar()
        self.activity = StringVar()

        labelTicketNo = ttk.Label(self.tab1,text="TicketNo.",font=("游ゴシック",15))
        labelActivity = ttk.Label(self.tab1,text="Activity",font=("游ゴシック",15))
        labelComment = ttk.Label(self.tab1,text="Comment",font=("游ゴシック",15))
        labelTime = ttk.Label(self.tab1, text = "Dummy", font=("游ゴシック", 15))

        self.entryTicketNo = ttk.Entry(self.tab1, width = 13, font=("游ゴシック", 15), textvariable=self.ticketNo)
        self.entryComment = ttk.Entry(self.tab1, width = 13, font=("游ゴシック", 15), textvariable=self.comment)
        self.comboBoxActivity = ttk.Combobox(self.tab1, state = 'readonly', width = 13, font=("游ゴシック", 15), textvariable = self.activity)
        self.canvasProgress = Canvas(self.tab1, width = 300, height = 350)

        labelTicketNo.place(x = 20, y = 80)
        labelActivity.place(x = 20, y = 150)
        labelComment.place(x = 20, y = 220)
        labelTime.place(x = 400, y = 150)

        self.entryTicketNo.place(x = 130, y = 80)
        self.entryComment.place(x = 130, y = 220)
        self.comboBoxActivity.place(x = 130, y = 150)
        self.canvasProgress.place(x = 300, y = 0)

        self.progressBar = CircularProgressBar(self.canvasProgress, 10, 20, 300, 300, 30)
        self.progressBar.initControl()

        redmineData = RedmineData
        activityTaple = redmineData.getActivityTaple()
        self.comboBoxActivity["values"] = activityTaple
        pass


    def createColleagues(self):
        """
        メンバー(相談役に相談するメンバー)の設置
        """
        self.startButton = ColleagueButton("start", self.tab1, self)
        self.stopButton = ColleagueButton("stop", self.tab1, self)
        self.pauseButton = ColleagueButton("pause",self.tab1, self)

        self.startButton.bind('<Button-1>', self.actionExecute)
        self.stopButton.bind('<Button-1>', self.actionExecute)
        self.pauseButton.bind('<Button-1>', self.actionExecute)

        self.pauseButton.place(x = 70, y = 300)
        self.startButton.place(x = 140, y = 300)
        self.stopButton.place(x = 210, y = 300)
        pass


    def colleagueChanged(self):
        """
        ボタンの網掛け制御
        """
        #スタートボタン押下時
        if str(self.startButton['state']) == 'disabled':
            if str(self.stopButton['state']) == 'disabled':
                if str(self.pauseButton['state']) == 'disabled':
                    self.pauseButton.configure(state = NORMAL)
                    self.stopButton.configure(state = NORMAL)

        #一時停止ボタン押下時
        if str(self.pauseButton['state']) == 'disabled':
            if str(self.startButton['state']) == 'disabled':
                self.startButton.configure(state = NORMAL)
                self.stopButton.configure(state = NORMAL)

        #停止ボタン押下時
        if str(self.stopButton['state']) == 'disabled':
            if str(self.startButton['state']) == 'disabled':
                self.startButton.configure(state = NORMAL)
                self.pauseButton.configure(state = DISABLED)
        pass

    @abstractmethod
    def actionExecute(self, event):
        pass

    @abstractmethod
    def initializeCreation(self):
        pass

    @abstractmethod
    def executeEntry(self, *args):
        pass