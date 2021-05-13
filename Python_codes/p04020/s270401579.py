N=int(input())
pre=int(input())
ans=pre//2
pre=pre&1
for i in range(2,N+1):
    Ai=int(input())
    if pre and Ai>=1:
        ans+=1
        Ai-=1
    ans+=Ai//2
    pre=Ai&1
print(ans)