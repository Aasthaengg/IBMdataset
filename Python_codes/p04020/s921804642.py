N = int(input())
A = [int(input()) for i in range(N)]

ans = 0
rest = 0
for a in A:
    ans += (a + rest) // 2
    rest = 1 if (a + rest) % 2 == 1 and a > 0 else 0

print(ans)