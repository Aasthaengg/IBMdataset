n=int(input())
a=[]
a=list(map(int,input().split()))
ave=sum(a)/n
if ave<int(ave)+0.5:
  ave=int(ave)
else:
  ave=int(ave)+1
ans=0
for i in range(n):
  ans+=(a[i]-ave)**2
print(ans)