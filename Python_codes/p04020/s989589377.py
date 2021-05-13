N=int(input())
ans=0
s=0
for i in range(1,N+1):
    Ai=int(input())
    if Ai==0:
        ans+=s//2
        s=0
    else:
        s+=Ai
ans+=s//2
print(ans)