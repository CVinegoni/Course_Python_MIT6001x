
###
# File: exam.py
# Project: ps6
# File Created: Wednesday, 31st July 2019 3:50:01 am
# Author: C.V (vinegoni@yahoo.com)
# -----
# Last Modified: Wednesday, 31st July 2019 3:50:02 am
# Modified By: C.V (vinegoni@yahoo.com)
# -----
# Copyright 2019 - C.V
###


def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False


def swapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)


L = [1, 10, 3, 5, 2, 20, 4, 20, 7]
e = 2
print(swapSort(L))
