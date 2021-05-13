n = int(input())
a = list(map(int,input().split()))
ans = int(1e18)
for i in range(101):
    cnt = 0
    for j in range(n):
        cnt += (a[j]-i)**2
    ans = min(ans,cnt)
    cnt = 0
    for j in range(n):
        cnt += (a[j]+i) **2
    ans = min(ans,cnt)
print(ans)
