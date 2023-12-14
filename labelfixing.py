import os

path = '/Users/meryemecedal/Desktop/facemaskdet/yolov5/datasets/facemaskdet/labels/x'
os.chdir('/Users/meryemecedal/Desktop/facemaskdet/yolov5/datasets/facemaskdet/labels/x')
xxx = os.listdir()

for file in xxx:
   if file.find('.txt') > -1:
       filename = file[0:file.index('.')]
       with open(file,'r+') as f:
           #print(f)
           
           print("\n")
           print(filename)
           print("\n")
          
           contents = f.read()
           print(contents)
           print("\n")
           
           s = contents.split(" ")
           print(s)
           print("\n")
           
           new = []
           for i in range (0, 5):
               if i is int(0):
                   si = int(s[i])
               else:
                   si = float(s[i]) * 0.25
               print("\n")
               print(si)
                   
               new.append(si)
               
           print("\n")
           print(new)
           print("\n")
           
           b = str(new)
           print(b)
           b = b.replace('[', '')
           b = b.replace(']', '')
           b = b.replace(',', '')
           print("\n")
           print(b)       
           
           n = open(filename + '.txt', 'w+')
           n.write(b)
           print(n)
           
           n.close()
       
       


    
