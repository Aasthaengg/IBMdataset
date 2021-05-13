# coding: utf-8
# Your code here!
n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
ans=0
for i in range(n):
    ans+=min(l[2*i],l[2*i+1])
print(ans)
