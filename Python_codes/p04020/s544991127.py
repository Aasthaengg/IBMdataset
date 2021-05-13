N = int(input())
A = [int(input()) for _ in range(N)]

ans = 0
rest = 0
for i, a in enumerate(A):
    if rest == 0:
        ans += a // 2
        rest = a % 2
    else:
        if (a + rest) % 2 == 0:
            ans += (a + rest) // 2
            rest = 0
        else:
            ans += (rest + a) // 2
            rest = 1 if a != 0 else 0

print(ans)
