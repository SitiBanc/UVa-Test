# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 20:40:51 2017

@author: sitibanc
"""

# UVa 11332
x = int(input())
while(x != 0):
    while(x >= 10):
        y = 0
        while(x > 0):
            y = y + x % 10
            x = x //10
        x = y
        print(x)
    x = int(input())