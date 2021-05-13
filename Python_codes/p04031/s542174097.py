N=int(input())
a=list(map(int,input().split()))
maxi=max(a)
mini=min(a)
ans1=(maxi**2)*N
for i in range(mini,maxi+1):
    ans=0
    for j in a:
        ans+=abs(j-i)**2
    if ans<ans1:
        ans1=ans
print(ans1)
