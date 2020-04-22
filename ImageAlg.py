from cv2 import cv2 as cv2
from PyQt5.QtGui import QPixmap, QImage
import pytesseract
import numpy as np
import time
from collections import deque

def showImage(img, title='Image'):
    cv2.namedWindow(title)
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def color2gray(img):
    if len(img.shape) == 2:
        return img
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def ostu(img, bottom=127, head=255):
    img = color2gray(img)
    res, thresh1 = cv2.threshold(img, bottom, head, cv2.THRESH_BINARY)
    return thresh1

def drawPoly(img, pts):
    neoImg = img.copy()
    color=((0,0,0), (255,0,0), (0,255,0), (0,0,255))
    for i in range(4):
        cv2.line(neoImg, pts[i], pts[(i+1)%4],color[i], 2)
    return neoImg

def drawRectangle(img, point1, point2, color=(255,255,255)):
    #to show the selected image content
    return cv2.rectangle(img, point1, point2, color, 3)

def CounterClockwiseRotate(img, angle):
    #roate
    angle = angle%360
    rows, cols = img.shape[:2]
    m = cv2.getRotationMatrix2D(((cols)/2, (rows)/2), angle, 1)
    return cv2.warpAffine(img,m, (rows, cols))

def cutImage(img, leftUpPoint, rightDownPoint):
    return img[leftUpPoint[1]:rightDownPoint[1], leftUpPoint[0]:rightDownPoint[0]]

def CannyEdge(img, minVal = 50, maxVal=150):
    img = color2gray(img)
    img = cv2.GaussianBlur(img, (3,3), 0)
    canny = cv2.Canny(img, minVal, maxVal)
    return canny

def RevengeColor(img):
    return cv2.bitwise_not()

def CorrectPerspective(img, pts):
    ptsVec = np.float32(pts)
    width = img.shape[1]
    height = img.shape[0]
    ptsVec2 = np.float32(((0,0), (width, 0), (width, height), (0, height)))
    matrix = cv2.getPerspectiveTransform(ptsVec, ptsVec2)
    result = cv2.warpPerspective(img, matrix, (width, height))
    return result
def ocr(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return pytesseract.image_to_string(img_rgb, lang='chi_sim')

class Image():
    def __init__(self, path):
        self.__img = cv2.imread(path)
        self.__path = path
        self.__history = deque()
        self.count = 1
        self.curTime = str(time.time())
    def Save(self):
        cv2.imwrite(self.__path, self.__img)
    def SaveAs(self, newPath):
        cv2.imwrite(newPath, self.__img)
        self.__path = newPath
    def getPath(self):
        return self.__path
    def getWidth(self):
        return self.__img.shape[1]
    def getHeight(self):
        return self.__img.shape[0]
    def getImg(self):
        return self.__img
    def setImg(self, transform):
        self.__history.append(self.__img)
        self.__img = transform(self.__img)
        self.curTime = time.time()
    def getTime(self):
        return self.curTime
    def undoImg(self):
        self.curTime = str(time.time())
        print("有生之年")
        self.count  +=1
        if len(self.__history) != 0:
            self.__img = self.__history[len(self.__history)-1]
            self.__history.pop()
            print("爷的青春回来了"+ str(self.count))
        else:
            print("爷的青春结束了"+str(self.count))
    def getPixmap(self):
        #height, width, bytesPerComponent = self.__img.shape
        width = self.__img.shape[1]
        height = self.__img.shape[0]
        bytesPerline = width*3
        neoImage = cv2.cvtColor(self.__img, cv2.COLOR_BGR2RGB)
        qimg = QImage(neoImage.data, width, height, bytesPerline, QImage.Format_RGB888)
        return QPixmap.fromImage(qimg)

if __name__ == "__main__":
    img = Image("lena.jpg")
    pts = [(10,100),(40,200), (205,400), (350,300)]
    pts.sort(key=lambda x: (x[0], x[1]))
    img.setImg(lambda img:drawPoly(img, pts))
    showImage(img.getImg())
