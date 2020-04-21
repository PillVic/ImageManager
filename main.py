import sys
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap, QImage
from ImageAlg import *
from ImageLabel import ImageLabel

class ImageManager(QMainWindow):
    pts = []
    def __init__(self):
        super(ImageManager, self).__init__()
        loadUi('neoMainWindow.ui', self)
        #loadUi('MainWindow.ui', self)
        #init UI
        #load Image
        fileName = QFileDialog.getOpenFileName(self, "Choose File", "")[0]
        if fileName == "":
            sys.exit()
        self.statusBar().showMessage("Open File : "+fileName)
        self.image = Image(fileName)
        self.imageMap = self.findChild(ImageLabel, "imageMap")
        self.imageMap.setPixmap(self.image.getPixmap())
        self.imageMap.setScaledContents(True)
        #set fresh task
        self.timer = QTimer(self)
        self.timer.setInterval(100) #100ms 
        self.timer.start()
        self.timer.timeout.connect(self.__fresh)
        self.curTime = self.image.getTime()
        
        #File Menu
        self.fileOpen = self.findChild(QAction, "fileOpen")
        self.fileOpen.triggered.connect(self.__open)

        self.fileSave = self.findChild(QAction, "actionSave")
        self.fileSave.triggered.connect(self.image.Save)

        self.fileSaveAs = self.findChild(QAction, "actionSaveAs")
        self.fileSaveAs.triggered.connect(self.__SaveAs)

        self.actionExit = self.findChild(QAction, "actionExit")
        self.actionExit.triggered.connect(sys.exit)
        #Edit Menu
        self.actionUndo = self.findChild(QAction, "actionUndo")
        self.actionUndo.triggered.connect(self.image.undoImg)

        #button set
        self.undoButton = self.findChild(QPushButton, "undoButton")
        self.undoButton.clicked.connect(self.image.undoImg)

        self.selectButton = self.findChild(QPushButton, "selectButton")
        #fixme

        self.grayButton = self.findChild(QPushButton, "grayButton")
        self.grayButton.clicked.connect(lambda x:self.image.setImg(color2gray))

        self.edgeDecButton = self.findChild(QPushButton, "edgeDecButton")
        self.edgeDecButton.clicked.connect(lambda x:self.image.setImg(CannyEdge))

        self.ostuBottom = self.findChild(QSpinBox, "ostuBottom")
        self.ostuFloor = self.findChild(QSpinBox, "ostuFloor")
        self.ostuButton = self.findChild(QPushButton, "ostuButton")
        self.ostuButton.clicked.connect(lambda x:self.image.setImg(lambda img: ostu(img, self.ostuBottom.value(), self.ostuFloor.value())))

        self.handleSelectButton = self.findChild(QPushButton, "handleSelectButton")
        self.handleSelectButton.clicked.connect(self.__handleSelect)
        self.imageMap.polyDone.connect(self.__drawPoly)

        
    def __drawPoly(self):
        self.pts.clear()
        w, h = self.image.getWidth(), self.image.getHeight()
        points = self.imageMap.getPts()
        #change the locate to image locate
        for i in points:
            point = int(i[0]*w/512), int(i[1]*h/649)
            self.pts.append(point)
        self.image.setImg(lambda img:drawPoly(img, self.pts))
    def __fresh(self):
        if self.curTime != self.image.getTime():
            self.imageMap.setPixmap(self.image.getPixmap())
    def __open(self):
        fileName = QFileDialog.getOpenFileName(self, "Choose File", "")[0]
        if fileName != "":
            self.image = Image(fileName)
    def __SaveAs(self):
        fileName = QFileDialog.getSaveFileName(self, "Choose File", "")[0]
        if fileName != "":
            self.image.SaveAs(fileName)
    def __handleSelect(self):
        self.imageMap.setPoly()



if __name__=="__main__":
    app = QApplication(sys.argv)
    widget = ImageManager()
    widget.show()
    sys.exit(app.exec_())
