# -*- coding : utf-8 -*-

N = int(input())
L = list(map(int, input().split()))

L.sort()
m = min(L)
M = max(L)

A = []
for i in range(m,M+1):
  k=0
  for j in L:
    k += (j-i)*(j-i)
  A.append(k)
  
print(min(A))