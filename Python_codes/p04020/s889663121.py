n = int(input())
ans = 0
tmp = 0
for i in range(n):
    k = int(input())
    if k:
        tmp += k
    else:
        ans += tmp // 2
        tmp = 0
print(ans + tmp // 2)
