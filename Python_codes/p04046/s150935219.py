H, W, A, B = map(int, input().split())
mod = int(1e+9 + 7)
p = mod - 2
X, Y = H-A, W-B
L = []
while p != 0:
  L = [p%2] + L[:]
  p //= 2
S = 0
fL = [1]
invfL = []
for i in range(H+W):
  fL.append(((i+1)*fL[i])%mod)
for i in range(H):
  invi = 1
  for j in range(len(L)):
    if L[j] == 1:
      invi *= fL[i]
      invi %= mod
    if j != len(L)-1:
      invi *= invi
      invi %= mod
  invfL.append(invi)
invB = 1
invW = 1
for i in range(len(L)):
  if L[i] == 1:
    invB *= fL[B-1]
    invB %= mod
    invW *= fL[W-B-1]
    invW %= mod
  if i != len(L)-1:
    invB *= invB
    invB %= mod
    invW *= invW
    invW %= mod
for i in range(X):
  S += (fL[i+B-1]*fL[H+Y-i-2]*invfL[i]*invfL[H-i-1])%mod
  S %= mod
print((S*invB*invW)%mod)