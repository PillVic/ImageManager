import cv2

def showImage(img, title='Image'):
    cv2.namedWindow(title)
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def color2gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


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
    def save(self):
        cv2.imwrite(self.__path, self.__img)
    def getWidth(self):
        return self.__img.shape[0]
    def getHeight(self):
        return self.__img.shape[1]
    def getImg(self):
        return self.__img
    def setImg(self, transform):
        self.__img = transform(self.__img)

if __name__ == "__main__":
    img = Image('lena.jpg')
    img.setImg(lambda x:CounterClockwiseRotate(x, 15)) 
    img.setImg(CannyEdge)
    showImage(img.getImg())
