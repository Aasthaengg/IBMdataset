#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import division, print_function, absolute_import, unicode_literals

def main():
    N, L = list(map(int, input().split()))
    a = list(map(int, input().split()))
    pair_L = []
    for car, cdr in zip(a[:-1], a[1:]):
        pair_L.append(car + cdr)
    maximum = max(pair_L)
    # print(maximum)
    if maximum < L:
        print("Impossible")
    else:
        print("Possible")
        index = pair_L.index(maximum) + 1
        i = 1
        while i < index:
            print(i)
            i += 1
        i = N - 1
        while i > index:
            print(i)
            i -= 1
        print(index)

if __name__ == "__main__":
    main()
