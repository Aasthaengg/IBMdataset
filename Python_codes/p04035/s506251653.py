n, l = map(int, input().split())
a = list(map(int, input().split()))
ans = float("inf")
for i in range(n - 1):
    if a[i] + a[i + 1] >= l:
        ans = i + 1
if ans == float("inf"):
    print("Impossible")
else:
    print("Possible")
    print(*range(1, ans), sep="\n")
    print(*range(n - 1, ans, -1), sep="\n")
    print(ans)