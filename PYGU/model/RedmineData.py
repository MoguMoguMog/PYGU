'''
Created on 2018/11/04

@author: mog
'''
from redminelib import Redmine
from redminelib.exceptions import ResourceNotFoundError
import datetime
from tkinter.constants import ACTIVE

class RedmineData():
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.redmine = Redmine('http://localhost:81/redmine', username='ishikawa', password='yuto1004')

    def setTicketNo(self, ticketNo):
        """
        チケットNoの設定
        """
        self.ticketNo = ticketNo
        pass

    def getSpentHours(self):
        """
        チケットNoから現在の工数を取得する
        """
        issue = self.redmine.issue.get(int(self.ticketNo))
        return issue.spent_hours

    def getEstimatedHours(self):
        """
        チケットNoから予定工数を取得する
        """
        issue = self.redmine.issue.get(int(self.ticketNo))
        return issue.estimated_hours

    def sendInfoRedmine(self, ticketNo, spentHours, activityKey, comment):
        """
        Redmineに工数情報を送る
        """
        # 日付の取得
        today = datetime.datetime.today()

        timeEntry = self.redmine.time_entry.new()
        timeEntry.issue_id = ticketNo
        timeEntry.spent_on = datetime.date(int(today.year), int(today.month),int(today.day))
        timeEntry.hours = spentHours
        timeEntry.activity_id = self.getActivityList()[activityKey]
        timeEntry.comments = comment

        timeEntry.save()

    def getActivityList(self):
        """
        活動のリスト取得
        """
        activityTaple = self.getActivityTaple()
        activityList = {activityTaple[0]:8, activityTaple[1]:9}
        return activityList

    @staticmethod
    def getActivityTaple():
        """
        活動のタプル取得
        """
        activityTaple = ("", "設計作業", "開発作業")
        return activityTaple