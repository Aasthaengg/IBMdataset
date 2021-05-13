inp=input().split(" ")
H=int(inp[0])
W=int(inp[1])
A=int(inp[2])
B=int(inp[3])
mod=10**9+7
fact=[1]
fact_r=[1]
for i in range(1,H+W-1):
    fact.append(i*fact[i-1]%mod)
    fact_r.append(pow(fact[i],10**9+5,mod))
const=fact_r[H-A-1]*fact_r[A-1]%mod
ans=sum(fact[H+i-A-1]*fact_r[i]*fact_r[W-i-1]*fact[W-i-2+A]%mod for i in range(B,W))
print(ans*const%mod)