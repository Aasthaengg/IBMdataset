import numpy as np
hi = np.zeros((5000,60),np.int64)
hi[0,0]=1
n,a = map(int, input().split())
li = [int(it) for it in input().split()]
for i in li:
    hi_ = hi.copy()
    hi[i:-1,1:]+=hi_[:-1-i,:-1]
s = 0
for i in range(n):
  s+=hi[(i+1)*a,i+1]
print (s)