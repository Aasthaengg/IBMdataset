n=int(input())
a=list(map(int,input().split()))
ans=float("inf")
for i in range(-100,101):
    k=0
    for j in a:
        k+=(j-i)**2
    ans=min(ans,k)
print(ans)