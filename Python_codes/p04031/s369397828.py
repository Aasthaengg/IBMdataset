n=int(input())
lst=list(map(int,input().split()))
ave=sum(lst)/n
if ave%1>=0.5:
    import math
    ave=math.ceil(ave)
else:
    ave//=1
ans=0
for i in lst:
    ans+=(abs(i-ave))**2
print(int(ans))