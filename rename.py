#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:44:29 2022

@author: meryemecedal
"""

import os

path = '/Users/meryemecedal/Desktop/face_recognition_frames_copy/Ahmet Ertuğ Darendelioğlu'

files = os.listdir(path)

print(files)


for i in range(100):
    file1 = "Ahmet Ertuğ Darendelioğlu_1_" + str(i) + ".txt"
    file2 = "Ahmet Ertuğ Darendelioğlu_1_" + str(i) + ".jpg"
    
    new1 = "Ahmet Ertug Darendelioglu_1_" + str(i) + ".txt"
    new2 = "Ahmet Ertug Darendelioglu_1_" + str(i) + ".jpg"
    
    try:
        f = os.rename(file1, new1)
        f = os.rename(file2, new2)
        
    
    
#    f = f.find("Ertuğ Darendelioğlu")
#    x = f.replace("Ertuğ Darendelioğlu","Ertug Darendelioglu")





