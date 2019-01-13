'''
Created on 2018/10/22

@author: mog
'''
#! /usr/bin/env python

from tkinter import *
from tkinter import ttk

from control.CIddTab1 import CIddTab1
from view.RIddTab1 import RIddTab1
from control.CIddTab2 import CIddTab2


class BaseLayer(ttk.Frame):
    """
    コントロール以外(フレーム等)の設定クラス
    """

    def __init__(self, master=None):
        """
        コンストラクタ
        """
        super().__init__(master)
        self.master.title('APP')
        self.master.geometry('600x400+0+0')
        self.master.resizable(0,0)
        self.initNotebook()
        CIddTab1(self.tab1)
        CIddTab2(self.tab2)
        pass

    def initNotebook(self):
        """
        ノートブックの設置
        """
        self.notebook = ttk.Notebook(width = 570, height = 350)
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text = 'Timer', padding=3)
        self.notebook.add(self.tab2, text = 'Table', padding=3)
        self.notebook.add(self.tab3, text = 'Statistics', padding=3)
        self.notebook.pack(expand=1, fill='x', anchor='n')
        pass

if __name__ == '__main__':
    root = Tk()
    BaseLayer(root)
    root.mainloop()

