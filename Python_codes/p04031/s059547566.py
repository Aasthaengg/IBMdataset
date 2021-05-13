n = int(input())
a = list(map(int, input().split()))
ave = sum(a)//n
ave1 = ave + 1
ans = 0
ans1 = 0
for i in range(n):
    ans += (a[i] - ave)**2
    ans1 += (a[i] - ave1)**2
print(min(ans, ans1))