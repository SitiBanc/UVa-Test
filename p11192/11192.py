# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 20:53:32 2017

@author: sitibanc
"""

# UVa 11192

x = input()
tmp = x.split()
num = int(tmp[0])
while(num != 0):
    str = tmp[1]
    count = len(str)//num
    for i in range(0, len(str), count):
        for j in range(0, count):
            print(str[i + count],end='')
    print('')
    x = input()
    tmp = x.split()
    num = int(tmp[0])