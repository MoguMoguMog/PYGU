'''
Created on 2018/11/23

@author: mog
'''
from view.RIddTab2 import RIddTab2
import tkinter.messagebox as tkmsg
from redminelib import Redmine
from model.RedmineData import RedmineData
from tkinter import *
from tkinter import ttk
from redminelib.exceptions import ResourceNotFoundError

class CIddTab2(RIddTab2):
    '''
    Tableタブの制御クラス
    '''

    def __init__(self, tab2):
        '''
        Constructor
        '''
        super().__init__(tab2)
        self.initializeCreation()

    def actionExecute(self, event):
        """
        ボタン押下時の処理
        """
        if (event.widget["text"] == "send"):
            self.executeSendButton()
        pass

    def executeSendButton(self):
        """
        送信ボタン押下時
        """
        try:
            for redmineData in self.redmineDataList:
                ticketNo = redmineData[0].get()
                activity = redmineData[1].get()
                time = redmineData[2].get()
                comment = redmineData[3].get()

                if ticketNo != "" and activity != "" and time != "":
                    print("in")
                    redmine = RedmineData()
                    print("redmine")
                    # 工数、活動、コメント情報をRedmineに送信
                    redmine.sendInfoRedmine(ticketNo, time, activity, comment)

                    redmineData[0].delete(0, END)
                    redmineData[1].current(0)
                    redmineData[2].delete(0, END)
                    redmineData[3].delete(0,END)
        except:
            tkmsg.showerror('入力エラー', "不正な入力値です。")

    def initializeCreation(self):
        pass


