from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import pyqtSignal
import cv2
class ImageLabel(QLabel):
    pts = []
    getPoly = False
    polyDone = pyqtSignal(str)
    #鼠标点击事件
    def mousePressEvent(self,event):
        point = event.pos().x(), event.pos().y()
        if self.getPoly == False:
            return
        self.pts.append(point)
        print(self.pts)
        if len(self.pts) == 4 and self.getPoly:
            self.getPoly = False
            self.polyDone.emit("points get")
    def getPts(self):
        return self.pts
    def setPoly(self):
        self.pts.clear()
        self.getPoly = True
