import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap, QImage
from ImageAlg import *

class ImageManager(QMainWindow):
    def __init__(self):
        super(ImageManager, self).__init__()
        loadUi('MainWindow.ui', self)
        fileName = QFileDialog.getOpenFileName(self, "Choose File", "")[0]
        self.statusBar().showMessage("Open File : "+fileName)
        self.__image = Image(fileName)
        self.imageLable = self.findChild(QLabel, "imageLable")
        self.imageLable.setPixmap(self.__image.getPixmap())
        self.imageLable.setScaledContents(True)


if __name__=="__main__":
    app = QApplication(sys.argv)
    widget = ImageManager()
    widget.show()
    sys.exit(app.exec_())