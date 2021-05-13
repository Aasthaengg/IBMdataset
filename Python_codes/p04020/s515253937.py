N = int(input())
A = [int(input()) for i in range(N)]

ans = 0
part_sum = 0
for i in range(N):
    if A[i] == 0 or i == N-1:
        part_sum += A[i]
        ans += (part_sum // 2)
        part_sum = 0
    else:
        part_sum += A[i]

print(ans)




