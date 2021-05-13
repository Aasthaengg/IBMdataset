n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
ans=0
for i in range(0,len(l)-1):
    if i%2==0:
        ans+=min(l[i],l[i+1])

print(ans)

