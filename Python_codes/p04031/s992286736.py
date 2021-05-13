n = int(input())
a = list(map(int,input().split()))
ans=10**9
for i in range(-100,100+1):
    const=0
    for j in a:
        const += (j-i)**2
    ans=min(ans,const)
print(ans)