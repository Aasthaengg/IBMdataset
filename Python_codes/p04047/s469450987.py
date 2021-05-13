n = int(input())
ls = list(map(int, input().split()))

ls.sort(reverse=True)

ans = 0

for i in range(n):
    ans += ls[2 * i + 1]

print(ans)