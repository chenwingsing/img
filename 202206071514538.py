#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#随机拼接像素，每次图片拼接的像素点都不一样
import itertools
import random
from PIL import Image
import os
import glob
import math
def generatepoint(x1,x2,y1,y2,n,file_name):#n代表一共多少个坐标
    random_list = list(itertools.product(range(x1, x2), range(y1, y2)))
    f = open(r'mix/val/'+file_name.replace('jpg','txt'),'w+')
    a = random.sample(random_list, n)
    for i in range(n):
        print(a[i][0],a[i][1],file=f)




def getInts(ln):
    return [int(word) for word in ln.split()]


def getRGB(file_path,pointrecord):#可以得到图片的RGB具体值
    print(len(pointrecord))
    (filepath, file_name) = os.path.split(file_path)
    newimage = Image.new("RGB", (224, 224))
    im = Image.open(file_path)
    rgb_im = im.convert('RGB')
    rgbrecord = []
    for x in range(len(pointrecord)):
        r, g, b = rgb_im.getpixel((pointrecord[x][0], pointrecord[x][1]))#找出对应坐标的RGB
        temp = []
        temp.append(int(r))
        temp.append(int(g))
        temp.append(int(b))
        rgbrecord.append(temp)
    count = 0
    length = int(math.sqrt(len(pointrecord)))
    for i in range(length):
        for j in range(length):
            newimage.putpixel((i, j), (rgbrecord[count][0], rgbrecord[count][1], rgbrecord[count][2]))
            count = count + 1
    newimage.save(r'../speckle_data/10-v1/speckle/valrandom'+'//'+file_name)



if __name__ == '__main__':
    path = r"../speckle_data/10-v1/speckle/val"#目标图片的路径
    all_file = glob.glob(os.path.join(path,'*jpg'))
    for i in range(len(all_file)):
        pointrecord = []
        file_path,file_name = os.path.split(all_file[i])
        generatepoint(40,380,40,320,224*224,file_name)
        f = open(r'mix/val/'+file_name.replace('jpg','txt'))  # 输入坐标保存位置
        pointrecord = [getInts(ln) for ln in f]  # 把所有坐标找出来
        f.close()
        getRGB(all_file[i],pointrecord)







