H,W,A,B = map(int,input().split())

mod = 10**9 + 7

f = [1]
for i in range(H+W):
    f.append(f[i]*(i+1)%mod)

def comb(A,B,mod):
    return f[A] * pow(f[B],mod-2,mod) * pow(f[A-B],mod-2,mod) % mod

res = 0

for i in range(B,W):
    res += comb(H-A+i-1,i,mod) * comb(A+W-i-2,A-1,mod) % mod

print(res%mod)