from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

N,L = inpl()
aa = inpl()
tmp = 0
for i in range(N-1):
	if aa[i] + aa[i+1] >= L:
		tmp += 1
		ind = i+1

if tmp == 0:
	print('Impossible')
else:
	print('Possible')
	for i in range(1,ind):
		print(i)
	for i in reversed(range(ind,N)):
		print(i)
