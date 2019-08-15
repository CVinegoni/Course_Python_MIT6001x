
# File: exam-03.py
# Project: ps6
# File Created: Tuesday, 6th August 2019 8:28:54 am
# Author: C.V (vinegoni@yahoo.com)
# -----
# Last Modified: Tuesday, 6th August 2019 8:28:54 am
# Modified By: C.V (vinegoni@yahoo.com)
# -----
# Copyright 2019 - C.V
###


def print_without_vowels(s=''):

    converted = ''
    for ch in s:
        if ch not in 'aeiouAEIOU':
            converted += ch
    print(converted)


if __name__ == "__main__":
    s = ""
    print_without_vowels(s)
