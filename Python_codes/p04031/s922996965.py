n=int(input())
a=list(map(int,input().split()))
ma=max(a)
mi=min(a)
ans=10**9

for i in range(mi,ma+1):
    tm=0
    for j in a:
        tm+=(j-i)**2
    else:
        ans=min(ans,tm)

print(ans)

