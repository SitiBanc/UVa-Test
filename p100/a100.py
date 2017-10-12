#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 13:30:55 2017

@author: sitibanc
"""

ans = [0] * 10000001
ans[1] = 1
def myF(n, tmp):
    # To prevent index out of range

    # The answer of myF(n) has already been recorded in the answer list
    if ans[n] != 0:
        return ans[n]
    # Tha answer of myF(n) hasn't been calculated
    if n % 2 == 0:
        count = myF(n//2, tmp)
    else:
        if 3 * n + 1 > 1000000:
            dbgF(tmp)
        else:
            count = myF(3*n+1, tmp)
    ans[n] = count 
    count = 0
    return ans[n]

def dbgF(n):
    count = 1
    while n > 1:
        if n % 2 == 0:
            count += 1
            n = n // 2
        else:
            count += 1
            n = 3 * n + 1
    return count

n = 0
while n < 100:
    inStr = input().split()
    
    maxN = myF(int(inStr[1]), 0)
    start = min(int(inStr[0]), int(inStr[1]))
    end = max(int(inStr[0]), int(inStr[1]))
    for i in range(start, end):
        if myF(i, i) > maxN:
            maxN = myF(i, 0)
    print(inStr[0], inStr[1], maxN)
    n += 1