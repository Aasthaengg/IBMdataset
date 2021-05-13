H,W,A,B = map(int, input().split())

mod = 10**9+7
fact = [1]
for i in range(1, H+W+1):
    fact.append ( fact[-1] * i % mod)

inv_fact = [0] * (H+W+1)
inv_fact[H+W] = pow(fact[H+W], mod-2, mod)

for i in range(H+W, 1, -1):
    inv_fact[i-1] = inv_fact[i] * i % mod

inv_fact[0] = 1

def C(a,b):
    if a <= 0 or b < 0:
        return 0
    if a==0 or b == 0:
        return 1
    return fact[a] * inv_fact[b] * inv_fact[a-b] % mod

ans = 0
for w in range(B+1, W+1):
    h = H-A - (w-B-1)
    if w == 0 or h == 0:
        break
    ans = (ans + C(h+w-2, w-1) * C(H+W-h-w, W-w) % mod) % mod
print(ans)