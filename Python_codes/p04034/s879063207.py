import numpy as np

n,m = map(int,input().split())
l = []
for _ in range(m):
    a = list(map(int,input().split()))
    l.append(a)

memo = np.zeros((n,2))
memo[0][1] = 1

for i in range(n):
    memo[i][0] = 1

tmp1 = 0
tmp2 = 0

for j in range(m):
    tmp1 = l[j][0]-1
    tmp2 = l[j][1]-1
    memo[tmp1][0] -= 1
    memo[tmp2][0] += 1
    
    if memo[tmp2][1] == 0 and memo[tmp1][1] == 1:
        memo[tmp2][1] = 1
    
    if memo[tmp1][1] == 1 and memo[tmp1][0] == 0:
        memo[tmp1][1] = 0

ans = 0
for k in range(n):
    ans += memo[k][1]

print(int(ans))
