n=int(input())
l=sorted(map(int,input().split()))
ans=0
while len(l)>1:
    ans+=min(l.pop(),l.pop())
print(ans)