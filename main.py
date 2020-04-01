import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from PyQt5.uic import loadUi

class ImageManager(QMainWindow):
    def __init__(self):
        super(ImageManager, self).__init__()
        loadUi('MainWindow.ui', self)
        fileName = QFileDialog.getOpenFileName(self, "Choose File", "")[0]
        self.statusBar().showMessage("Open File : "+fileName)

if __name__=="__main__":
    app = QApplication(sys.argv)
    widget = ImageManager()
    widget.show()
    sys.exit(app.exec_())