#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:11:21 2017

@author: sitibanc
"""

def getTimes(str2):
    times = [0]
    i = 0
    while i < len(str2):
        if str2[i].isdecimal():
            if str2[i+1].isdecimal():
                times.append(int(str2[i]) * 10 + int(str2[i+1]))
                i += 1  # Skip next digit
            else:
                times.append(int(str2[i]))
        i += 1
    return times

case = 1
n = int(input())
while case <= n:
    try:
        str1 = input() + ' '
    except EOFError:
        break
    j = 1
    times = getTimes(str1)
    check = False
    for k in str1:
        if k.isalpha():
            check = True
            break
    if check:
        print('Case ' + str(case), end=': ')
        case += 1
    for i in range(len(str1) - 1):
        if str1[i].isalpha():
            print(str1[i] * times[j], end='')
            j += 1
    print('')