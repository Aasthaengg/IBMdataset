# -*- coding: utf-8 -*-
 
import math
import itertools
import sys
import copy
#import numpy as np
 
# 入力
#A, B, C, D = map(int, input().split())
#L = list(map(int, input().split()))
#S = list(str(input()))
#N = int(input())
#S = str(input())

N = int(input())
L = list(map(int, input().split()))

L.sort()
ans = 0
for i in range(0, N*2, 2) :
  ans += L[i]
  
print (ans)

