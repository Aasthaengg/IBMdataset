n=int(input())
a=list(map(int,input().split()))
ans=10000000
for i in range(-100,101):
    tmp=0
    for j in range(n):
        tmp+=(a[j]-i)**2
    if tmp<ans:
        ans=tmp
print(ans)