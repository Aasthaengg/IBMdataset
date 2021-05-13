n, a = map(int, input().split())
x = list(map(lambda x: int(x) - a, input().split()))
d = {0: 1}
for i in x:
    for j, k in list(d.items()):
        d[i + j] = d.get(i + j, 0) + k
ans = d[0] - 1
print(ans)
