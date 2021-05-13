import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(input())
from collections import Counter
c = Counter(S)

if (c['N']==0 and c['S']!=0) or (c['N']!=0 and c['S']==0) or (c['E']==0 and c['W']!=0) or (c['E']!=0 and c['W']==0):
    print('No')
else:
    print('Yes')