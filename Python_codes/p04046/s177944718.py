import sys
H,W,A,B = map(int,sys.stdin.readline().rstrip().split())
mod = 10**9+7

kaijou = [1]
for i in range(1,H+W-1):
    kaijou.append((kaijou[-1]*i) % mod)

a = 0
for i in range(B):
    b = kaijou[(H-A-1)+i]*pow(kaijou[i],mod-2,mod)*pow(kaijou[H-A-1],mod-2,mod)
    b %= mod
    b *= kaijou[(W+A-2)-i]*pow(kaijou[A-1],mod-2,mod)*pow(kaijou[W-1-i],mod-2,mod)
    b %= mod
    a += b
    a %= mod

c = kaijou[H+W-2]*pow(kaijou[H-1],mod-2,mod)*pow(kaijou[W-1],mod-2,mod)
c %= mod

print((c-a) % mod)