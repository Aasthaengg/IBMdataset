n = int(input())
a = [int(input()) for _ in range(n)]
ans = 0
cur_sum = 0  # 0が入るまでのsum
for i in range(n):
    if a[i] == 0:
        ans += cur_sum // 2
        cur_sum = 0
    else:
        cur_sum += a[i]
ans += cur_sum // 2
print(ans)
