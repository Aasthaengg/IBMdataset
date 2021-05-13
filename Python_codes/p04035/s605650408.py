import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    n,l = map(int,ipt().split())
    a = [int(i) for i in ipt().split()]
    pa = a[0]
    mi = -1
    for i,ai in enumerate(a[1::]):
        if pa+ai >= l:
            print("Possible")
            mi = i
            break
        pa = ai
    if mi == -1:
        print("Impossible")
        exit()
    for i in range(mi):
        print(i+1)
    for i in range(n-mi-1):
        print(n-i-1)

    return

if __name__ == '__main__':
    main()
