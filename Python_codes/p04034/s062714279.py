n, m = map(int, input().split())

ans = {1}
l = [1] * n

for i in range(m):
    x, y = map(int, input().split())
    l[x - 1] -= 1
    l[y - 1] += 1

    if x in ans:
        if l[x - 1] == 0: ans.remove(x); ans.add(y)
        else: ans.add(y)
print(len(ans))