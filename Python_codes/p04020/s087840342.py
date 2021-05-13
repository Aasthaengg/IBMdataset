N = int(input())
pre = int(input())
ans = pre // 2
for _ in range(N - 1):
    i = int(input())
    if pre % 2 == 1 and i > 0:
        i -= 1
        ans += 1
    ans += i // 2
    pre = i
print(ans)
