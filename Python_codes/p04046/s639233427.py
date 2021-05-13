h,w,a,b=map(int,input().split())
factorials=[]
inverses=[]
MOD=10**9+7
factorials.append(1)
curr=1
for i in range(1,h+w+1):
  curr=(curr*i)%MOD
  factorials.append(curr)
for i in range(h+w+1):
  inverses.append(pow(factorials[i],MOD-2,MOD))
ans=0
for i in range(h-a):
  ans=(ans+factorials[b-1+i]*factorials[h-2-i+w-b]*inverses[i]*inverses[b-1]*inverses[h-1-i]*inverses[w-b-1])%MOD
print(ans)