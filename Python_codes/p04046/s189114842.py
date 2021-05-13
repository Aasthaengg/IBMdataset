MOD=10**9+7
H,W,A,B=map(int,input().split())

def invmod(a):
  return pow(a,MOD-2,MOD)
def comb_mod(n,r):
  return fact_dic[n]*fact_inv_dic[r]*fact_inv_dic[n-r]

fact_dic={0:1}
fact_inv_dic={0:1}
fact_mod=1
for i in range(1,H+W-1):
  fact_mod=(fact_mod*i)%MOD
  fact_dic[i]=fact_mod
  fact_inv_dic[i]=invmod(fact_mod)
  
answer=0
if H-A>=W-B:
  for i in range(B,W):
    answer+=comb_mod(H-A+B-1,i)*comb_mod(W+A-B-1,W-1-i)
    answer%=MOD
else:
  for j in range(H-A):
    answer+=comb_mod(H-A+B-1,B+j)*comb_mod(W+A-B-1,W-B-1-j)
    answer%=MOD
    
print(answer)