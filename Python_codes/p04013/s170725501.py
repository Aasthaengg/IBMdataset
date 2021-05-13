n,a=map(int,input().split())
import numpy as np
x=np.array(input().split(),dtype=int)
x-=a
pluslist=[]
minuslist=[]
zerocnt=0
for i in range(len(x)):
  if x[i]==0:
    zerocnt+=1
  elif x[i]>0:
    pluslist.append(x[i])
  else:
    minuslist.append(x[i]*(-1))

dpplus=np.full((sum(pluslist)+1),0,dtype=int)
dpminus=np.full((sum(minuslist)+1),0,dtype=int)
dpplus[0]=1
dpminus[0]=1
for v in pluslist:
  for i in range(len(dpplus)-1,-1,-1):
    if dpplus[i]!=0:
      dpplus[i+v]+=dpplus[i]
for v in minuslist:
  for i in range(len(dpminus)-1,-1,-1):
    if dpminus[i]!=0:
      dpminus[i+v]+=dpminus[i]

ans=2**zerocnt-1
for i in range(1,min(len(dpplus),len(dpminus))):
  ans+=dpplus[i]*dpminus[i]*(2**zerocnt)
  
print(ans)