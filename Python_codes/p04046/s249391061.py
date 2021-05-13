h, w, a, b = map(int, input().split())
mod = 1000000007

def modpow(x, y):   
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return modpow(x, y//2)**2 % mod
    else            : return modpow(x, y//2)**2 * x % mod

stairs = [1]
for i in range(1, h+w+1):
    stairs.append(stairs[i-1]*i%mod)

inverse_stairs = [0]*(h+w)
inverse_stairs[h+w-1] = modpow(stairs[h+w-1], mod-2)
for i in range(h+w-2, -1, -1):
    inverse_stairs[i] = inverse_stairs[i+1] * (i+1) % mod
    
ret = 0
for i in range(w-b):
    com = stairs[w-i+h-a-2]%mod
    com = com*inverse_stairs[w-i-1]%mod
    com = com*inverse_stairs[h-a-1]%mod
    com = com*stairs[i+a-1]%mod
    com = com*inverse_stairs[i]%mod
    com = com*inverse_stairs[a-1]%mod
    ret += com

print(ret%mod)