import cv2
import os

path = '/Users/meryemecedal/Desktop/facemaskdet/yolov5/datasets/facemaskdet/images/x'
os.chdir('/Users/meryemecedal/Desktop/facemaskdet/yolov5/datasets/facemaskdet/images/x')
xxx = os.listdir()

for file in xxx:
   if file.find('.jpg') > -1:
       #print(file)
       img = cv2.imread(file)
       #cv2.imshow("img", img)
       
       filename = file[0:file.index('.')]
       #print(filename)            
       if img.shape[1] == 2160:
           scale_percent = 0.125
           width = int(img.shape[1]*scale_percent)
           height = int(img.shape[0]*scale_percent)
           dimension = (width, height)
           
           resized = cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)
           
           print(resized.shape)
           
           cv2.imshow('output', resized)
           
           cv2.imwrite(filename + '.jpg', resized)
       else:
           pass
       
   else:
       pass
        


# print("Done!")
# cv2.waitKey(0)
# cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # fileName = file[28:file.index('.')]
    # print('\n')
    # print(fileName)


    # scale_percent = 0.33
    # width = int(img.shape[1]*scale_percent)
    # height = int(img.shape[0]*scale_percent)
    # dimension = (width, height)
    
    # resized = cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)
    
    # print(resized.shape)
    # cv2.imshow('output', resized)
    # cv2.imwrite(fileName, resized)