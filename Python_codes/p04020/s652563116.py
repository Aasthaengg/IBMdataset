n=int(input())
ans=0
cnt=0
for i in range(n):
    a=int(input())
    if a==0:
        ans+=cnt//2
        cnt=0
    else:
        cnt+=a
ans+=cnt//2
print(ans)
