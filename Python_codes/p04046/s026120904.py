H,W,A,B = map(int,input().split())
MOD = (10**9)+7
D = [0,2, 9, 11, 14, 15, 17, 19, 20, 23, 24, 25, 27, 28, 29]

def inv(a):
    ans = 1
    hoge = a
    for count in range(31):
        if (count) in D:
            ans *= hoge
            ans %= MOD
        hoge *= hoge
        hoge %= MOD
    return ans

g = [1]*(H+W)
for i in range(1,H+W):
    g[i] = (g[i-1]*i%MOD)
ans = 0
for i in range(H-A):
    L = g[B-1+i]*inv(g[B-1])*inv(g[i])
    R = g[(W-B-1)+(H-1-i)]*inv(g[(W-B-1)])*inv(g[H-1-i])
    ans += L*R%MOD
print(ans%MOD)