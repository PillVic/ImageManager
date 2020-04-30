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
        self.__open()
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
        self.actionChange2Gray = self.findChild(QAction, "actionChange2Gray")
        self.actionChange2Gray.triggered.connect(lambda x:self.image.setImg(color2gray))
        self.actionCannyEdgeDetect = self.findChild(QAction, "actionCannyEdgeDetect")
        self.actionCannyEdgeDetect.triggered.connect(lambda x:self.image.setImg(CannyEdge))

        #button set
        self.undoButton = self.findChild(QPushButton, "undoButton")
        self.undoButton.clicked.connect(self.image.undoImg)

        self.reloadButton = self.findChild(QPushButton, "reloadButton")
        self.reloadButton.clicked.connect(self.__reload)
        #fixme

        self.grayButton = self.findChild(QPushButton, "grayButton")
        self.grayButton.clicked.connect(lambda x:self.image.setImg(color2gray))

        self.edgeDecButton = self.findChild(QPushButton, "edgeDecButton")
        self.edgeDecButton.clicked.connect(lambda x:self.image.setImg(CannyEdge))

        self.binarizationBottom = self.findChild(QSpinBox, "binarizationBottom")
        self.binarizationFloor = self.findChild(QSpinBox, "binarizationFloor")
        self.binarizationButton = self.findChild(QPushButton, "binarizationButton")
        self.binarizationButton.clicked.connect(lambda x:self.image.setImg(lambda img: binarization(img, self.binarizationBottom.value(), self.binarizationFloor.value())))

        self.handleSelectButton = self.findChild(QPushButton, "handleSelectButton")
        self.handleSelectButton.clicked.connect(self.imageMap.setPoly)
        self.imageMap.polyDone.connect(self.__drawPoly)
        self.correctButton = self.findChild(QPushButton, "correctButton")
        self.correctButton.clicked.connect(lambda x:self.image.setImg(lambda img:CorrectPerspective(img, self.pts)))

        self.ocrButton = self.findChild(QPushButton, "ocrButton")
        self.textEdit = self.findChild(QTextEdit, "textEdit")
        self.ocrButton.clicked.connect(self.ocrPrint)
    def ocrPrint(self):
        text = ocr(self.image.getImg())
        self.textEdit.setText(text)
    def __reload(self):
        path = self.image.getPath()
        self.image = Image(path)
    def __drawPoly(self):
        self.pts.clear()
        w, h = self.image.getWidth(), self.image.getHeight()
        points = self.imageMap.getPts()
        for i in points:
            point = int(i[0]*w/self.imageMap.width()), int(i[1]*h/self.imageMap.height())
            self.pts.append(point)
        self.image.setImg(lambda img:drawPoly(img, self.pts))
    def __fresh(self):
        if self.curTime != self.image.getTime():
            self.imageMap.setPixmap(self.image.getPixmap())
            self.curTime = self.image.getTime()
    def __open(self):
        fileName = QFileDialog.getOpenFileName(self, "Choose File", "")[0]
        if fileName != "":
            self.image = Image(fileName)
            self.statusBar().showMessage("Image Name : "+fileName)
            height = self.image.getHeight()
            width = self.image.getWidth()
            self.pts = [(0,0), (width, 0), (width, height), (0, height)]
    def __SaveAs(self):
        fileName = QFileDialog.getSaveFileName(self, "Choose File", "")[0]
        if fileName != "":
            self.image.SaveAs(fileName)
            self.statusBar().showMessage("Image Name : "+fileName)



if __name__=="__main__":
    app = QApplication(sys.argv)
    widget = ImageManager()
    widget.show()
    sys.exit(app.exec_())
