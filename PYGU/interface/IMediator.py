'''
Created on 2018/11/04

@author: mog
'''
# coding: UTF-8

from abc import ABCMeta, abstractmethod

class IMediator(metaclass = ABCMeta):
    '''
    相談役のAPIを定めるインタフェース。
    '''
    @abstractmethod
    def createColleagues(self):
        pass

    @abstractmethod
    def colleagueChanged(self):
        pass
