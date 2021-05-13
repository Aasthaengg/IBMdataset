n=input()
a=input().split()
a=[int(i) for i in a]
a.sort()
count=0
ans=0
for i in a:
  if count%2==0:
    ans+=i
  count+=1
print(ans)