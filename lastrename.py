#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 12:39:35 2022

@author: meryemecedal
"""

import os

os.chdir('/Users/meryemecedal/Desktop/face_recognition_frames_copy/Ahmet Ertuğ Darendelioğlu')

for f in os.listdir():
    #print(f)
    
    #print(os.path.splitext(f))
    
    filename, ext = os.path.splitext(f)
    #print(filename)
    
    #print(filename.split('_'))
    name, idnumber, index = filename.split('_')
    #print(name)
    
    name1 = name.replace('Ertuğ Darendelioğlu', 'Ertug Darendelioglu') 
    #print(name1)
    
    print('{}_{}_{}{}'.format(name1, idnumber, index, ext))
    