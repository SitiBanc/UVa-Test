#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 02:05:11 2017

@author: sitibanc
"""

# Define a recursive function to calculate the (n3 + 1 algorithm) value of n
table = [0] * 1000001
table[1] = 1
def calValue(n):
    try:
        # Value n has already been calculated
        if table[n] != 0:
            return table[n]
    # Index out of range
    except IndexError:
        pass
    # Value n has yet to be calculated
    if n % 2 == 0:
        count = calValue(n // 2)
    else:
        count = calValue(3 * n + 1)
        
    try:
        table[n] = count + 1
        return table[n]
    except:
        print(n)
    
n = input()
while n != '':
    n = n.split()
    n0 = int(n[0])
    n1 = int(n[1])
    nMax = calValue(n1)
    for i in range(min(n0, n1), max(n0, n1)):
        print('Current i : ', i)
        try:
            nMax = max(nMax, calValue(i))
        except:
            print('nMax : ', nMax)
    print(n0, n1, nMax)
    n = input()