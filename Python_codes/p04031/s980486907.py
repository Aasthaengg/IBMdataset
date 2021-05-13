n=int(input())
a=list(map(int,input().split()))
ans=float('inf')
for i in range(-100, 101):
    tmp=0
    for j in range(n):
        tmp+=(i-a[j])**2
    ans=min(tmp,ans)
print(ans)
