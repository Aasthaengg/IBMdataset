n = int(input())
a = list(map(int, input().split()))
mean = round(sum(a) / n)
ans = 0
for i in a:
    ans = ans + (i-mean)**2
print(ans)