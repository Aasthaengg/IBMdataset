H, W, A, B = map(int, input().split())
answer = 0
mod = 1000000007
factorial = [1]
for n in range(1, H+W):
    factorial.append(factorial[n-1]*n%mod)
def power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x % mod
    elif y % 2 == 0:
        return power(x, y//2) ** 2 % mod
    else:
        a = power(x, y//2) ** 2
        return a * x % mod
inverseFactorial = [0] * (H+W)
inverseFactorial[H+W-1] = power(factorial[H+W-1], mod-2)
for n in range(H+W-2, -1, -1):
    inverseFactorial[n] = inverseFactorial[n+1] * (n+1) % mod
def combi(n, m):
    return factorial[n] * inverseFactorial[m] *inverseFactorial[n-m]%mod

for i in range(B+1, W+1):
    answer = (answer + combi(H-A-2+i, i-1)*combi(A+W-i-1,W-i)) % mod
print(answer)