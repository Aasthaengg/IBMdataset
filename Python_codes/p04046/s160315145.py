import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    h,w,a,b = map(int,ipt().split())
    mod = 10**9+7

    #nCrをmodで割った余りを求める。Nに最大値を入れて使用。
    N = 2*10**5
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル
    def cmb(n,r,mod):
        if r<0 or r>n :
            return 0
        r = min(r,n-r)
        return g1[n]*g2[r]*g2[n-r]%mod
    for i in range(2,N+1):
        g1.append((g1[-1]*i)%mod)
        inverse.append((-inverse[mod % i]*(mod//i))%mod)
        g2.append((g2[-1]*inverse[-1])%mod)

    ans = cmb(h+w-2,h-1,mod)
    for i in range(max(a,b)):
        ans = (ans-cmb(b+h-a-1,b-1-i,mod)*cmb(a+w-b-1,a-1-i,mod)%mod)%mod
    print(ans)



    return

if __name__ == '__main__':
    main()
