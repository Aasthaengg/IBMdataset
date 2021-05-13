N, *A = map(int, open(0).read().split())

r = 0
ans = 0
for a in A:
    if a == 0:
        r = 0
        continue
    q, r = divmod(a + r, 2)
    ans += q
print(ans)
