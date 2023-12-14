#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 01:35:36 2022

@author: meryemecedal
"""


import os
 
# Get the list of all files and directories
path = "/Users/meryemecedal/Desktop/face_recognition_frames_copy"

files = os.listdir(path)

for f in files:
	#print(f)
    new_f = f.replace('ü', 'u')
    print(new_f)
print('\n')
    
for f in new_f:
    new_f2 = f.replace('ç', 'c')
    print(new_f2)
    




#name = 'Batuhan Güler'

#print(name)

#new = name.replace('ü', 'u')
#print(new)