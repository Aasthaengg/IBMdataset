N = int(input())
part_sum = 0
ans = 0
for i in range(N):
    a = int(input())
    if a == 0 or i == N - 1:
        part_sum += a
        ans += part_sum // 2
        part_sum = 0
    else:
        part_sum += a
print(ans)