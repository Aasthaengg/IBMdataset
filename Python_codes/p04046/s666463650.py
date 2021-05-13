h, w, a, b = map(int, input().split())
mod = 10 ** 9 + 7

ans = 0
for i in range(1, h-a+1):
    if i == 1:
        t1 = 1
        t2 = 1
        for j in range(1, ((h-a-i)+(b-1)+1)):
            t1 *= j
            t1 %= mod
        for j in range(1, ((b-1)+1)):
            t2 *= j
            t2 %= mod
        for j in range(1, ((h-a-i)+1)):
            t2 *= j
            t2 %= mod
        a1 = t1 * pow(t2, mod-2, mod) % mod

        t1 = 1
        t2 = 1
        for j in range(1, ((w-b-1)+(a+i-1)+1)):
            t1 *= j
            t1 %= mod
        for j in range(1, ((w-b-1)+1)):
            t2 *= j
            t2 %= mod
        for j in range(1, ((a+i-1)+1)):
            t2 *= j
            t2 %= mod
        a2 = t1 * pow(t2, mod-2, mod) % mod
    else:
        a1 *= pow((h-a-i)+(b-1)+1, mod-2, mod) 
        a1 *= h-a-i+1
        a1 %= mod 
        a2 *=  (w-b-1)+(a+i-1) 
        a2 %= mod
        a2 *= pow(a+i-1, mod-2, mod) 
        a2 %= mod
 
    #print(a1, a2)
    ans += a1 * a2 
    ans %= mod

print(ans)

