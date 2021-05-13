class mod_comb_k():
  def __init__(self, MAX_N = 10**6, mod = 10**9+7):
    self.fact = [1]
    self.fact_inv = [0] * (MAX_N + 4)
    self.mod = mod
    if MAX_N > mod:print('MAX_N > mod !')
    for i in range(MAX_N + 3):
      self.fact.append(self.fact[-1] * (i + 1) % self.mod)
    self.fact_inv[-1] = pow(self.fact[-1], self.mod - 2, self.mod)
    for i in range(MAX_N + 2, -1, -1):
      self.fact_inv[i] = self.fact_inv[i + 1] * (i + 1) % self.mod
  def comb(self, n, k):
    if n < k:
      print('n < k !')
      return 0
    else:return self.fact[n] * self.fact_inv[k] % self.mod * self.fact_inv[n - k] % self.mod
h,w,a,b=map(int,input().split())
c=mod_comb_k()
mod=10**9+7
ans=c.comb(h+w-2,w-1)
for i in range(b):
  ans-=(c.comb(i+h-a-1,i)*c.comb(a+w-2-i,a-1))%mod
print(ans%mod)