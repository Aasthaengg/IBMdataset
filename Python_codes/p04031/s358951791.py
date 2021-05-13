n=int(input())
lis=list(map(int,input().split()))
ave=0
ans=0
for i in lis:
  ave+=i
ave/=n
if ave>=int(ave)+0.5:
  ave=int(ave)+1
else:
  ave=int(ave)
for i in lis:
  ans+=(i-ave)**2
print(ans)