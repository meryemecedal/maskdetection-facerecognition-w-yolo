import os
import shutil

path = '/Users/meryemecedal/Desktop/project/repos/labelImg/data/datas'
os.chdir('/Users/meryemecedal/Desktop/project/repos/labelImg/data/datas')
xxx = os.listdir()
datas = []
for xx in xxx:
    if xx.find('DS_Store') > -1:
        continue
    else:
        datas.append(xx)
for data in datas:
    os.chdir(data)
    files = os.listdir()
    for file in files:
        if file.find('classes') > -1:
            continue
        else:
            if file.find('txt') > -1:
                shutil.copy(path + '/' + data + '/' + file, '/Users/meryemecedal/Desktop/facemaskdet/yolov5/datasets/facemaskdet/labels')
            else:
               pass
                #shutil.copy(path + '/' + data + '/' + file, '/Users/meryemecedal/Desktop/facemaskdet/yolov5/datasets/facemaskdet/images')
    print(data)
    os.chdir('..')