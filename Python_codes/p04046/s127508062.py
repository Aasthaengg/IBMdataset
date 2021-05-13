H,W,A,B = map(int,input().split())
MOD = 10**9 + 7
FAC = [1]
INV = [1]
for i in range(1,H+W+1):
  FAC.append((FAC[i-1]*i) % MOD)
  INV.append(pow(FAC[-1],MOD-2,MOD))
#print(FAC)
#print(INV)

def nCr(n,r):
  return FAC[n]*INV[n-r]*INV[r]

ans = 0
for i in range(H-A):
  ans += nCr(i+B-1,min(i,B-1)) * nCr(H-i-1+W-B-1,min(H-i-1,W-B-1))
  ans %= MOD
print(ans)
