n = int(input())
a = [int(i) for i in input().split()]
num = int(sum(a) / len(a))
check = [num -3, num - 2, num -1, num, num + 1, num + 2, num +3]
ans = float('inf')
for i in check:
    cnt = 0
    for j in a:
        cnt += (i - j) ** 2

    ans = min(ans, cnt)
print(ans)