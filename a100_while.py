#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:53:25 2017

@author: sitibanc
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 02:05:11 2017

@author: sitibanc
"""

# Define a recursive function to calculate the (n3 + 1 algorithm) value of n
table = [0] * 1000001
table[1] = 1

try:
    n = input()
    while n != '':
        n = n.split()
        n0 = int(n[0])
        n1 = int(n[1])
        nMax = 0
        for i in range(min(n0, n1), max(n0, n1) + 1):
            count = 0
            j = i
            while table[j] == 0:
                if j % 2 == 0:
                    j = j // 2
                    count += 1
                else:
                    j = 3 * j + 1
                    count += 1
                while j > 1000000:
                    if j % 2 == 0:
                        j = j // 2
                        count += 1
                    else:
                        j = 3 * j + 1
                        count += 1
            if j != i:
                table[i] = table[j] + count
            nMax = max(nMax, table[i])
        print(n0, n1, nMax)
        n = input()
except EOFError:
    pass