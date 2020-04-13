from cv2 import cv2 as cv2
from PyQt5.QtGui import QPixmap, QImage

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
    img = Image('lena.jpg')
    #img.setImg(lambda x: ostu(x, 127, 255))
    img.setImg(lambda x:drawRectangle(x, (60,73), (451,275), (255,255,255)))
    image = img.getImg()
    neoimage = cutImage(image, (60,73), (451,275))
    img.SaveAs("SelectedImage.jpg")
    img.setImg(lambda x:neoimage)
    img.SaveAs("cutImage.jpg")
    