h, w, a, b = map(int,input().split())
mod = 10**9 + 7

def inv(x, p):
    pp = p-2
    ans = 1
    while pp > 0:
        if pp % 2 == 1:
            ans = (ans * x) % p
        x = (x ** 2) % p
        pp //= 2
    return ans

I = [1] + [inv(i, mod) for i in range(1, h+w+1)]

a0 = 1
a1 = 1
for i in range(w-b+a-1, (w-b+a-1)-(w-b-1), -1):
    a1 = (a1 * i) % mod
# print(a1)
for i in range(w-b-1+1):
    #print("i",i)
    a1 = (a1 * I[i]) % mod

A0 = [a0]
A1 = [a1]
for i in range(1, h-a):
    a0 = (a0 * (b-1+i)) % mod
    a0 = (a0 * I[i]) % mod
    A0.append(a0)

    a1 = (a1 * (w-b+a-1+i)) % mod
    a1 = (a1 * I[(w-b+a-1)-(w-b-1)+i]) % mod
    A1.append(a1)

# print(A0)
# print(A1)
ans = 0
for i in range(h-a):
    pl = (A0[i] * A1[-i-1]) % mod
    ans = (ans + pl) % mod

print(ans)