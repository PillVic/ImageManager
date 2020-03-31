import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class ImageManager(QMainWindow):
    def __init__(self):
        super(ImageManager, self).__init__()
        loadUi('MainWindow.ui', self)
        self.statusBar().showMessage("Ready to Read Image")
        self.ActionExit = self.findChild()

if __name__=="__main__":
    app = QApplication(sys.argv)
    widget = ImageManager()
    widget.show()
    sys.exit(app.exec_())