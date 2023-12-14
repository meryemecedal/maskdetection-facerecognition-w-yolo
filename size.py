import cv2
import glob

path = glob.glob('/Users/meryemecedal/Desktop/facemaskdet/yolov5/datasets/facemaskdet/images/*.jpg')


for file in path:
    print(file)
    
    
    img = cv2.imread(file)
   
    filename = file[75:file.index('.')]   
    
    scale_percent = 0.33
    width = int(img.shape[1]*scale_percent)
    height = int(img.shape[0]*scale_percent)
    dimension = (width, height)
    
    resized = cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)
    
    print(resized.shape)
    
    #cv2.imshow('output', resized)
    
    cv2.imwrite(filename, resized) 
   
    
   
    # cv2.imshow("Img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
    
 
    
 
    
 
    
 
    
# img = cv2.imread('Ahmet Can Polat_0_0.jpg')

# scale_percent = 0.33
# width = int(img.shape[1]*scale_percent)
# height = int(img.shape[0]*scale_percent)
# dimension = (width, height)

# resized = cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)

# print(resized.shape)
# cv2.imshow('output', resized)
# cv2.imwrite(a, resized)

# cv2.waitKey(0)
# cv2.destroyAllWindows()