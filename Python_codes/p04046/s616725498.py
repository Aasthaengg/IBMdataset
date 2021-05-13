MOD=10**9+7
H,W,A,B=map(int,input().split())

def invmod(a):
  return pow(a,MOD-2,MOD)
def comb_mod(n,r):
  if 0<=r<=n:
    return fact_dic[n]*fact_inv_dic[r]*fact_inv_dic[n-r]
  else:
    return 0

fact_dic={0:1}
fact_inv_dic={0:1}
fact_mod=1
for i in range(1,H+W-1):
  fact_mod=(fact_mod*i)%MOD
  fact_dic[i]=fact_mod
  fact_inv_dic[i]=invmod(fact_mod)
  
answer=0
for i in range(B,W):
  answer+=comb_mod(H-A-1+i,i)*comb_mod(A-1+W-1-i,W-1-i)
  answer%=MOD
    
print(answer)