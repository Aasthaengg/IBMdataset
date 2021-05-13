n = int(input())
a = list(map(int,input().split()))
ans = float('INF')
for i in range(-100,101):
    s = 0
    for j in range(n):
        s += (a[j]-i)**2
    ans = min(ans,s)
print(ans)