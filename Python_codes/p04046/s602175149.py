def mf(num,mod):
  ret=1
  for i in range(1,num+1):
    ret=(ret*i)%mod
  return ret

def rev(num,pow,mod):
  ret=1
  while pow>0:
    if pow&1!=0:
      ret=(ret*num)%mod
    pow=pow>>1
    num=(num*num)%mod
  return ret

h,w,a,b=map(int,input().split())
mod=10**9+7
ans=[]
s=0
tb=rev(mf(b,mod),mod-2,mod)
tf=mf(b-1,mod)
trev=[rev(mf(h-a-1,mod),mod-2,mod)]
for i in range(h-a-1,0,-1):
  trev.append((trev[h-a-1-i]*i)%mod)
trev=trev[::-1]
for i in range(h-a):
  tf=(tf*(b+i))%mod
  ans.append((tf*tb*trev[i])%mod)
  ans[i]=(ans[i]-s)%mod
  s+=ans[i]
tb=rev(mf(w-b-1,mod),mod-2,mod)
tf=mf(w+a-b-2,mod)
trev=[rev(mf(h-1,mod),mod-2,mod)]
for i in range(h-1,0,-1):
  trev.append((trev[h-1-i]*i)%mod)
for i in range(h-a-1,-1,-1):
  tf=(tf*(w-b-1+h-i-1))%mod
  ans[i]=(ans[i]*(tf*tb*trev[i])%mod)
ret=0
for i in range(h-a):
  ret+=ans[i]
  ret=ret%mod
print(ret)