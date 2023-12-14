#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 13:05:14 2022

@author: meryemecedal
"""


    
import os

path = '/Users/meryemecedal/Desktop/face_recognition_frames_copy/Özgür Özbey'

files = os.listdir(path)

for i in range(200):

    f2 = str(files[i]).replace("ğ", "g")
    f2 = f2.replace("ç", "c")
    f2 = f2.replace("ö", "o")
    f2 = f2.replace("ü", "u")
    f2 = f2.replace("ı", "i")
    f2 = f2.replace("ş", "s")
    # os.rename(str(files[i]), f1)
    os.rename(str(files[i]), f2)
    
    