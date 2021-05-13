N = int(input())
a = [int(input()) for _ in range(N)] + [0]
ans = 0

for i in range(N):
    if a[i] != 0:
        add, mod = divmod(a[i], 2)
        ans += add
        if a[i + 1] != 0:
            a[i + 1] += mod

print(ans)