'''
Created on 2018/11/04

@author: mog
'''
from redminelib import Redmine
from view.RIddTab1 import RIddTab1
from model.RedmineData import RedmineData
from tkinter import *
from tkinter import ttk
from redminelib.exceptions import ResourceNotFoundError

import tkinter.messagebox as tkmsg

class CIddTab1(RIddTab1):
    '''
    タイマータブの制御クラス
    '''

    def __init__(self, tab1):
        '''
        コンストラクタ
        '''
        super().__init__(tab1)
        self.initializeCreation()

    def initializeCreation(self):
        """
        画面表示初期化
        """
        self.initRedmineData()
        self.initializeAllView()

    def initRedmineData(self):
        """
        Redmine情報の初期化
        """
        self.redmine = None

    def initializeAllView(self):
        """
        コントロールの初期化
        """
        self.startButton.configure(state=DISABLED)
        self.stopButton.configure(state=DISABLED)
        self.pauseButton.configure(state=DISABLED)

    def actionExecute(self, event):
        """
        ボタン押下時の処理
        """
        if (event.widget["text"] == "start" and str(event.widget["state"]) == 'normal'):
            self.executeStartButton()

        elif (event.widget["text"] == "pause" and str(event.widget["state"]) == 'normal'):
            self.executePauseButton()


        elif (event.widget["text"] == "stop" and str(event.widget["state"]) == 'normal'):
            self.executeStopButton()

    def executeStartButton(self):
        """
        スタートボタンが押された時の処理
        """
        if (self.redmine == None):
            self.spentHours = 0
            self.redmine = RedmineData()
            # 入力されたチケットNoを設定
            self.redmine.setTicketNo(self.ticketNo.get())

            try:
                # Redmineからチケット工数を取得
                self.manHours = self.redmine.getSpentHours()
                # Redmineからチケットの予定工数を取得
                self.estimatedHours = self.redmine.getEstimatedHours()

            except (ValueError):
                tkmsg.showerror('チケットNoエラー', "不正な入力値です。")
                self.initRedmineData()
                pass
            except (ResourceNotFoundError):
                tkmsg.showerror('チケットNoエラー', "チケットが存在しません。")
                self.initRedmineData()

        self.entryTicketNo.configure(state=DISABLED)
        self.startButton.configure(state=DISABLED)
        self.pauseButton.configure(state=DISABLED)
        self.stopButton.configure(state=DISABLED)
        self.startButton.stateChanged()

        # 進捗バーに工数情報反映
        self.progressBar.setFullExtent(self.estimatedHours)
        self.progressBar.setManHours(self.manHours + self.spentHours)

        #タイマースタート
        self.progressBar.start()
        pass

    def executePauseButton(self):
        """
        一時停止ボタン押下時の処理
        """
        self.pauseButton.configure(state=DISABLED)
        self.pauseButton.stateChanged()

        # タイマーストップ
        self.progressBar.toggle_pause()

        # 工数の取得
        self.spentHours = self.progressBar.getManHours()

    def executeStopButton(self):
        """
        停止ボタン押下時の処理
        """
        self.entryTicketNo.configure(state=NORMAL)
        self.stopButton.configure(state=DISABLED)
        self.stopButton.stateChanged()

        # タイマーストップ
        self.progressBar.toggle_pause()
        # 工数の取得
        self.spentHours = self.progressBar.getManHours()

        try:
            # 工数、活動、コメント情報をRedmineに送信
            self.redmine.sendInfoRedmine(self.ticketNo.get(), self.spentHours, self.comboBoxActivity.get(), self.comment.get())

            self.entryTicketNo.delete(0, END)
            self.entryComment.delete(0, END)
            self.comboBoxActivity.current(0)
            self.redmine = None

            self.spentHours = 0
            self.manHours = 0
        except:
            tkmsg.showerror('Activity Error', "入力が不正です。")
            self.stopButton.configure(state=NORMAL)
            pass

    def executeEntry(self, *args):
        """
        チケットNo入力時の処理
        """
        #チケットNoが入力されたら
        if(self.ticketNo.get() != ""):
            self.startButton.configure(state=NORMAL)
        else:
            self.startButton.configure(state=DISABLED)

