# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 17:56:56 2017

@author: sitibanc
"""

import sys

def n3rule(n, clist):
    if n in clist:
        return clist[n]
        
    if n % 2 == 0:
        count_n = n3rule(n/2, clist)
    else:
        count_n = n3rule(3*n+1, clist)
    clist[n] = count_n + 1
    
    return clist[n]

def n3_max():
    clist = {1:1}
    for line in sys.stdin:
        i,j = map(int, line.split())
        max_count = 0
        for x in range(min(i,j), max(i,j)+1):
            max_count = max(n3rule(x, clist), max_count)
        print(i, j, max_count)

n3_max()