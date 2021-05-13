import numpy as np
import scipy.sparse as sps
import scipy.misc as spm
import collections as col
import functools as func
import itertools as ite
import fractions as frac
import math as ma
import copy as cp
import sys
def sinput(): return sys.stdin.readline()
def iinput(): return int(sinput())
def imap(): return map(int, sinput().split())
def fmap(): return map(float, sinput().split())
def iarr(): return list(imap())
def farr(): return list(fmap())
def sarr(): return sinput().split()

n,a = imap()
x = np.array(iarr()) - a

# dp[i][和 + NA]
# 本来のSの範囲は、1N-NAから50N-NA
# 負の数はdp範囲外なのでNAたすと、1Nから50N
# 和０のときは dp[n][0+NA]
dp = np.zeros((n+1, 50*n+1)).astype(int)
dp[0][n*a] = 1

for i in range(n):
    for s in range(50*n+1):
        dp[i+1][s] = dp[i][s] + dp[i][s-x[i]] if 50*n>= s-x[i] >=0 else dp[i][s]

ans = dp[n][n*a] - 1 #実際は初期条件の０個選ぶパターンを除外
print(ans)


