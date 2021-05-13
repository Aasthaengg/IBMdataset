n=int(input())
a=list(map(int,input().split()))
ans=10**18
for num in range(-100,101):
    cnt=0
    for i in range(n):
        cnt+=(num-a[i])**2
    ans=min(ans,cnt)
print(ans)