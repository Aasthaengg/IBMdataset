n,m = map(int, input().split())

'''
d = dict()
for i in range(1,n+1):
    d[str(i)] = 1
from collections import deque
ans = deque('1')'''
box = [1 for i in range(n)]
ans = [0 for i in range(n)]
ans[0] = 1
for _ in range(m):
    x,y = map(int,input().split())
    box[x-1] -= 1
    box[y-1] += 1
    if ans[x-1]==1 and ans[y-1]==0:
        ans[y-1] = 1
    if box[x-1]==0 and ans[x-1]==1:
        ans[x-1] = 0
print(sum(ans))
