n = int(input())
cnt = [0]*n
for i in range(n):
    a = int(input())
    cnt[i] += a

ans = 0
for i, j in zip(range(n-1), range(1, n)):
    x, y = cnt[i], cnt[j]
    z = x//2
    cnt[i] -= 2*z
    ans += z
    if cnt[i] == 0:
        continue
    if 0 < y:
        ans += 1
        cnt[i] -= 1
        cnt[j] -= 1
else:
    ans += cnt[-1]//2

print(ans)