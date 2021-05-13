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
    n = int(ipt())
    ans = 0
    pi = 0
    for _ in range(n):
        a = int(ipt())
        if a == 0:
            pi = 0
        else:
            ans += (pi+a)//2
            pi = (pi+a)%2
    print(ans)

    return

if __name__ == '__main__':
    main()
