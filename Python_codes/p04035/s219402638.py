n, l = map(int, input().split())
a = [int(i) for i in input().split()]
b = []
for i in range(n-1):
    b.append(a[i] + a[i+1])
if max(b) >= l:
    ans = "Possible"
else:
    ans = "Impossible"
print(ans)
if ans == "Possible":
    k = b.index(max(b))
    ans = list(range(1, k + 1)) + list(range(n - 1, k + 1, -1)) + [k + 1]
    for i in ans:
        print(i)