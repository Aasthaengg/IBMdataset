import sys
from collections import Counter
from collections import deque
import math
import bisect
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))


n=int(input())
l=[int(input()) for i in range(n)]
ans=0
c=0
for i in range(n):
    if l[i]==0:
        ans+=c//2
        c=0
    else:
        c+=l[i]
ans+=c//2
print(ans)