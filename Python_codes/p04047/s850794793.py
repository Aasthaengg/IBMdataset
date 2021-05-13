N = int(input())
a = sorted(list(map(int, input().split())))

res =[]
for i in range(N):
    res.append(a[2*i])

print(sum(res))