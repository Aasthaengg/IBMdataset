n=int(input())
a=[int(input()) for _ in range(n)]+[0]

ans=0
cnt=0

for aa in a:
    if aa==0:
        ans+=cnt//2
        cnt=0
    else:
        cnt+=aa

print(ans)