from cv2 import cv2 as cv2
from PyQt5.QtGui import QPixmap, QImage

def showImage(img, title='Image'):
    cv2.namedWindow(title)
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def color2gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def ostu(img, bottom=127, head=255):
    img = color2gray(img)
    res, thresh1 = cv2.threshold(img, bottom, head, cv2.THRESH_BINARY)
    return thresh1

def drawRectangle(img, point1, point2, color=(0,0,0)):
    #to show the cut image content
    return cv2.rectangle(img, point1, point2, color, 3)

def CounterClockwiseRotate(img, angle):
    #roate
    angle = angle%360
    rows, cols = img.shape[:2]
    m = cv2.getRotationMatrix2D(((cols)/2, (rows)/2), angle, 1)
    return cv2.warpAffine(img,m, (rows, cols))

def CannyEdge(img):
    img = color2gray(img)
    img = cv2.GaussianBlur(img, (3,3), 0)
    canny = cv2.Canny(img, 50, 150)
    return canny

class Image():
    def __init__(self, path):
        self.__img = cv2.imread(path)
        self.__path = path
    def Save(self):
        cv2.imwrite(self.__path, self.__img)
    def SaveAs(self, newPath):
        cv2.imwrite(newPath, self.__img)
    def getWidth(self):
        return self.__img.shape[0]
    def getHeight(self):
        return self.__img.shape[1]
    def getImg(self):
        return self.__img
    def setImg(self, transform):
        self.__img = transform(self.__img)
    def getPixmap(self):
        height, width, bytesPerComponent = self.__img.shape
        bytesPerline = width*3
        cv2.cvtColor(self.__img, cv2.COLOR_BGR2RGB, self.__img)
        qimg = QImage(self.__img.data, width, height, bytesPerline, QImage.Format_RGB888)
        return QPixmap.fromImage(qimg)

if __name__ == "__main__":
    img = Image('lena.jpg')
    #img.setImg(lambda x: ostu(x, 127, 255))
    img.setImg(lambda x:drawRectangle(x, (60,73), (451,275)))
    showImage(img.getImg())