#教程 https://www.jianshu.com/p/e10dc43c38d0
#文档 https://cloud.baidu.com/doc/OCR/s/Dk3h7yf8m

import cv2
import sys
from aip import AipOcr
import os

APP_ID = '19642725'
API_KEY = 'yCRtNOcWGuA9t4KhGGvN7lQq'
SECRET_KEY = 'Ej6RKH2w1w9kn6wbSIh3yRmWkEqAQvw0'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

rect_color = [(255,0,0), (0,255,0), (0,0,255)]

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def baiduocr(fname):
    image = get_file_content(fname)

    """ 调用通用文字识别（不含位置版） 50000次/天 """
    #results = client.basicGeneral(image)["words_result"]
    """ 调用通用文字识别（不含位置高精度版） 500次/天 """
    results = client.basicAccurate(image)["words_result"]

    fout = open('ocrresult.txt', 'w')
    for result in results:
        text = result["words"]
        print(text)

        fout.write(text+'\n')
    fout.close()


def baiduocr_location(fname):
    image = get_file_content(fname)

    options = {}
    options["recognize_granularity"] = "small"
    #options["detect_direction"] = "true"
    #options["vertexes_location"] = "true"
    #options["probability"] = "true"

    """ 调用通用文字识别（含位置版） 500次/天 """
    #results = client.general(image, options)["words_result"]
    """ 调用通用文字识别（含位置高精度版） 50次/天 """
    results = client.accurate(image, options)["words_result"]

    img = cv2.imread(fname)
    for result in results:
        text = result["words"]
        location = result["location"]
        print(text)

        chars = result["chars"]
        cnt = 0
        for ch in chars:
            location = ch["location"]
            # 画矩形框
            cv2.rectangle(img, (location["left"],location["top"]), (location["left"]+location["width"],location["top"]+location["height"]), rect_color[cnt%3], 2)
            cnt = cnt + 1

    cv2.imwrite(fname[:-4]+"_result.jpg", img)

def neoOcr(img):
    tempPath = r".temp.jpg"
    cv2.imwrite(tempPath, img)
    tempFile = get_file_content(tempPath)
    
    """ 调用通用文字识别（不含位置版） 50000次/天 """
    #results = client.basicGeneral(image)["words_result"]
    """ 调用通用文字识别（不含位置高精度版） 500次/天 """
    results = client.basicAccurate(tempFile)["words_result"]
    r = ""
    for i in results:
        r += i['words']
        r+='\n'
    os.remove(tempPath)
    return r

if __name__ == '__main__':
    if len(sys.argv) < 2:
        #命令格式: python  2.baiduocr.py  a.png
        #命令格式: python  2.baiduocr.py //默认识别pre_img.png
        print('默认识别pre_img.png')

    if len(sys.argv) < 2:
        pic_path = 'example/o4174.JPG'
    else:
        pic_path = sys.argv[1]

    baiduocr(pic_path)  #不带位置版
    #baiduocr_location(pic_path)  #带位置版