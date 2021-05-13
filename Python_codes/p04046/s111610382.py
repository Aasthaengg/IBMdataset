
def modinv(a, m): #mod. m でのaの逆元 a^{-1}を計算する
    b = m
    u = 1
    v = 0
    while b:
        t = a//b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    
    u %= m
    if u < 0:
        u += m
    return u

H, W, A, B = map(int, input().split())

MOD = 10 ** 9 + 7

#O(N)
first = []
for i in range(0, H - A):
    if i == 0:
        tmp = 1
        first.append(tmp)
        continue
    tmp = (tmp * (B + i - 1) * modinv(i, MOD)) % MOD
    first.append(tmp)

# print (first)

#O(N)
second = []
for i in range(0, H):
    if i == 0:
        tmp = 1
        second.append(tmp)
        continue
    tmp = (tmp * ((W - B) + i - 1) * modinv(i, MOD)) % MOD
    second.append(tmp)

# print (second)

#O(N)
ans = 0
for i in range(H - A):
    ans = (ans + first[i] * second[H - 1 -i]) % MOD

print (ans)
#total O(3 * N) --> O(N)