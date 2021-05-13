n = int(input())
a_ls = list(map(int, input().split()))
small = sum(a_ls)//n
big = small + 1
ans = float('inf')
for goal in [big, small]:
    Sum = 0
    for a in a_ls:
        Sum += (goal - a) ** 2
    ans = min(ans, Sum)
print(ans)