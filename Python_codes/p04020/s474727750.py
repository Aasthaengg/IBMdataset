n=int(input())

cnt=0
ans=0
for _ in range(n):
    a=int(input())

    if a>0:
        cnt+=a
    else:
        ans+=cnt//2
        cnt=0
    
print(ans+cnt//2)