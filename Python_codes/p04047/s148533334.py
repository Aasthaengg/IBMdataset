n = int(input())
l = list(map(int,input().split()))
l = sorted(l)[::-1]
res = 0
for i in range(1,2 * n,2):
    res += l[i]
print(res)