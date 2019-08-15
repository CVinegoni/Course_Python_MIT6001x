
# File: exam-04.py
# Project: ps6
# File Created: Tuesday, 6th August 2019 9:46:08 am
# Author: C.V (vinegoni@yahoo.com)
# -----
# Last Modified: Tuesday, 6th August 2019 9:46:08 am
# Modified By: C.V (vinegoni@yahoo.com)
# -----
# Copyright 2019 - C.V
###


def longest_run(L):
    up = 1
    sum = L[0]
    up_array = []
    sumup_array = []
    for j in range(len(L)-1):
        if L[j] >= L[j+1]:
            up += 1
            sum += L[j+1]
            up_array.append(up)
            sumup_array.append(sum)
        else:
            up = 1
            sum = L[j+1]
            up_array.append(up)
            sumup_array.append(sum)
    down = 1
    sum = L[0]
    down_array = []
    sumdown_array = []
    for j in range(len(L)-1):
        if L[j] <= L[j+1]:
            down += 1
            sum += L[j+1]
            down_array.append(down)
            sumdown_array.append(sum)
        else:
            down = 1
            sum = L[j+1]
            down_array.append(down)
            sumdown_array.append(sum)
    # print(up_array)
    # print(sumup_array)
    # print(down_array)
    # print(sumdown_array)
    m = (max(up_array))
    M = (max(down_array))
    if m > M:
        # print(up_array.index(m))
        return sumup_array[up_array.index(m)]
    elif m < M:
        # print(down_array.index(M))
        return sumdown_array[down_array.index(M)]
    elif m == M:
        if (up_array.index(m)) <= (down_array.index(M)):
            return sumup_array[up_array.index(m)]
        else:
            return sumdown_array[down_array.index(M)]


L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
L = [5, 4, 10]
print(longest_run(L))
