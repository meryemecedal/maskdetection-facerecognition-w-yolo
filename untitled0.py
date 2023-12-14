#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:44:35 2022

@author: meryemecedal
"""
i = 0
for i in range(100):
    dosyaismi = "Betül Avcıl_13_" + str(i) + ".txt"
    try:
        dosya = open(dosyaismi,"r",encoding="utf-8")
        oku = dosya.read()
        if len(oku) < 5:
            print("\n")
            print(dosyaismi)
            print("\n")
    except:
        pass
