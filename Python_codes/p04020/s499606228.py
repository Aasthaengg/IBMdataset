import sys

n, *aaa = map(int, sys.stdin.buffer.read().split())

ans = 0
for i in range(n - 1):
    d, m = divmod(aaa[i], 2)
    ans += d
    if m and aaa[i + 1]:
        aaa[i + 1] -= 1
        ans += 1
ans += aaa[-1] // 2
print(ans)
