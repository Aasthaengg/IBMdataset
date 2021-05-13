N, L = map(int, input().split())
Sn = [input() for _ in range(N)]

Sn_sort = sorted(Sn)
ans = ""

for i in Sn_sort:
    ans += i

print(ans)