# -*- coding: utf-8 -*-

import numpy as np

def main(p1,p2):
    L_np = np.sort(np.array(p2))
    x_total = 0
    for i in range(p1):
        x_total += L_np[2*i]
    print(x_total)

if __name__ == "__main__":
    #a = [int(input()) for i in range(5)]
    N = int(input())
    L = [int(item) for item in input().split()]
    main(N,L)