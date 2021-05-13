import math
n = int(input())
lis = list(map(int, input().split()))

avg1 = math.ceil(sum(lis)/len(lis))
avg2 = math.floor(sum(lis)/len(lis))

ans1 = 0
ans2 = 0
for i in lis:
    ans1 += (i-avg1)**2
    ans2 += (i-avg2)**2

print(min(ans1, ans2))
