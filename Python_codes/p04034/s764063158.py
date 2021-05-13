#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
from fractions  import gcd
#input=sys.stdin.readline
import bisect
n,m=map(int,input().split())
num=[1]*n
s=set()
s.add(1)
ans=1
for i in range(m):
    x,y=map(int,input().split())
    num[x-1]-=1
    num[y-1]+=1
    if x in s:
        if num[x-1]!=0 and y not in s:
          ans+=1
        elif num[x-1]==0:
          s.discard(x)
          if y in s:
            ans-=1
        s.add(y)
print(ans)