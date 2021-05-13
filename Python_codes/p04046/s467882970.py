#D問題
import math
H,W,A,B = map(int,input().split())
mod = 10**9 + 7

M = H+W-1
fact = [1 for i in range(M)]
for i in range(M):
    if i == 0:
        pass
    else:
        fact[i] = (fact[i-1]*i)%mod
        
refact = [1 for i in range(M)]
m = mod-2
b = bin(m)
b = b.lstrip("0b")
b = b[::-1]
m2 = len(b)
for i in range(M):    
    flog = [0 for j in range(m2)]
    for j in range(m2):
        if j == 0:
            flog[0] = fact[i]
        else:
            flog[j] = (flog[j-1]**2)%mod
    #print(flog)
    for j in range(m2):
        if b[j] == "1":
            refact[i]*=flog[j]
            refact[i]%=mod
            
row = B
wide = W-B
ans = 0
for i in range(wide):
    row = B+i
    C1 = (fact[H-A+row-1]*refact[H-A-1]*refact[row])%mod
    C2 = (fact[W+A-row-2]*refact[W-row-1]*refact[A-1])%mod
    #print(C1,C2)
    ans+=C1*C2
    ans%=mod

#print(fact)
#print(refact)

print(ans)