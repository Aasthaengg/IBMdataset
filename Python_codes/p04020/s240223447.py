N=int(input())
ans=0
t=0
for _ in range(N):
    A=int(input())
    if A==0:
        ans+=t//2
        t=0
    else:
        t+=A
ans+=t//2
print(ans)