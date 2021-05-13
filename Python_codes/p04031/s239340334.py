N = int(input())
a = list(map(int, input().split()))
res = 10**9
for i in range(-100,101):
    SUM = 0
    for j in range(len(a)):
        SUM += (i-a[j])**2
    if SUM < res:
        res = SUM
print(res)