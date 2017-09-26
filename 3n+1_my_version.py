# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 18:11:11 2017

@author: sitibanc
"""

def awesomeF(n):
    l = [n]
    while n>1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n+1
        l.append(n)
    print("length: ")
    print(len(l))
    return l

results = awesomeF(10)
print(results[-1])
