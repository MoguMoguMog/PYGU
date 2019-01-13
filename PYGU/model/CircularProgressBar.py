'''
Created on 2018/10/27

@author: mog
'''
from time import sleep

class CircularProgressBar(object):
    """
    円形進捗バークラス
    """
    # 0.25H単位での実績工数
    spentHours = 0
    # 秒数のカウント
    count = 0

    def __init__(self, canvas, x0, y0, x1, y1, width=2, start_ang=90):
        """
        コンストラクタ
        """
        self.canvas = canvas
        self.x0, self.y0, self.x1, self.y1 = x0+width, y0+width, x1-width, y1-width
        self.tx, self.ty = (x1+x0) / 2, (y1+y0) / 2
        self.width = width
        self.start_ang= start_ang

        self.running = False
        pass

    def initControl(self):
        """
        進捗バーの初期表示
        """
        self.extent = 0
        self.arc_id = self.canvas.create_arc(self.x0, self.y0, self.x1, self.y1,
                                             start=self.start_ang, extent=self.extent,
                                             width=self.width, style='arc')

        time = ''
        self.timeText = self.canvas.create_text(self.tx, self.ty, text=time,
                                                font=("游ゴシック", 15))

    def updateControl(self):
        """
        進捗バーの表示更新
        """
        self.extent = 360 * self.manHours / self.full_extent
        self.canvas.delete(self.arc_id)
        self.arc_id = self.canvas.create_arc(self.x0, self.y0, self.x1, self.y1,
                                             start = self.start_ang, extent = self.extent,
                                             width = self.width, style = 'arc', outline = '#87ceeb')

    def start(self):
        """
        タイマースタート
        """
        self.running = True
        #1秒間隔
        self.interval = 1000
        #増加角度
        self.increment = 360 * (1 / self.full_extent)

        self.canvas.after(self.interval, self.step, self.increment)
        pass

    def step(self, delta):
        """
        1秒ごとの表示更新
        """
        if self.running:
            hour = 0
            min = 0
            sec = 0

            self.count += 1
            if (self.count%900 == 0):
                self.spentHours += 0.25

            self.extent = (self.extent + delta) % 1800
            if self.extent < 360:
                self.canvas.itemconfigure(self.arc_id, extent=self.extent)
            else:
                self.canvas.itemconfigure(self.arc_id, extent=359.9)

            #工数割合の表示更新
            self.canvas.delete(self.timeText)
            percent = '{:.0f}%'.format(round(float(self.extent) / 360, 2) * 100)
            time = int(self.manHours + self.count)
            min, sec = divmod(time, 60)
            hour, min = divmod(min, 60)

            self.timeText = self.canvas.create_text(self.tx, self.ty, text=str(hour)+':'+str(min)+':'+str(sec)+'\n'+'  '+percent, font=("游ゴシック", 15))
            self.canvas.after(self.interval, self.step, delta)

    def toggle_pause(self):
        """
        停止
        """
        # 1秒以内に再開すると計測間隔が狂うため、1秒強制で待ち
        sleep(1)
        self.running = not self.running

    def setFullExtent(self, estimatedHours):
        """
        見積工数の取得
        """
        self.full_extent = estimatedHours * 60 * 60

    def setManHours(self, manHours):
        """
        現在までにかかった工数を設定
        """
        self.manHours = manHours * 60 * 60
        self.updateControl()

    def getManHours(self):
        """
        現在までにかかった工数の取得
        """
        return self.spentHours