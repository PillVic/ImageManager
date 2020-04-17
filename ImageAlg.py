from cv2 import cv2 as cv2
from PyQt5.QtGui import QPixmap, QImage
import pytesseract
import numpy as np

def showImage(img, title='Image'):
    cv2.namedWindow(title)
    #cv2.imshow(title, cv2.resize(img, (800,600)))
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
    for i in pts:
        cv2.circle(img, i, 5, (0,0,255), -1)
    ptsVec = np.float32(pts)
    width = img.shape[1]
    height = img.shape[0]
    ptsVec2 = np.float32(((0,0), (width, 0), (0, height), (width, height)))
    matrix = cv2.getPerspectiveTransform(ptsVec, ptsVec2)
    result = cv2.warpPerspective(img, matrix, (width, height))
    return result
def ocr(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return pytesseract.image_to_string(img_rgb)

class Image():
    def __init__(self, path):
        self.__img = cv2.imread(path)
        self.__path = path
        self.__history = []
        self.count = 1
    def Save(self):
        cv2.imwrite(self.__path, self.__img)
    def SaveAs(self, newPath):
        cv2.imwrite(newPath, self.__img)
        self.__path = newPath
    def getWidth(self):
        return self.__img.shape[0]
    def getHeight(self):
        return self.__img.shape[1]
    def getImg(self):
        return self.__img
    def setImg(self, transform):
        self.__history.append(self.__img)
        self.__img = transform(self.__img)
    def undoImg(self):
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
    img = Image("example/IMG_4174.JPG")
    img.setImg(lambda x:cv2.resize(x, (800,600)))
    img.setImg(lambda x:CorrectPerspective(x, ((7,96), (782,9), (37,482),(786,553))))
    img.setImg(color2gray)
    img.SaveAs("PerspectiveAlg1.jpg")
    #import pytesseract
    #print(pytesseract.image_to_string(img.getImg()))
    