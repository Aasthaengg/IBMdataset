from collections import defaultdict
n,m=map(int, input().split())
v = [0]*n
v[0]=1
ans = [1]*n
fi = 1
for i in range(m):
    a,b=map(int, input().split())
    ans[a-1]-=1
    ans[b-1]+=1
    if v[a-1]:
        v[b-1]=1
        fi+=1
    if ans[a-1]==0:
        v[a-1]=0
        fi-=1

print(sum(v))
