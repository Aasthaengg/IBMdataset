n, a = map(int, input().split())
x = list(map(int, input().split()))

for i in range(n):
    x[i] -= a

x.sort()

if x[0] > 0 or x[-1] < 0:
    print(0)
    exit()

num_zero = x.count(0)

if x[0] == 0 or x[-1] == 0:
    print(pow(2, num_zero) - 1)
    exit()

xp = [i for i in x if i > 0]
xm = [-i for i in x if i < 0]

sum_xp = sum(xp) + 1
dp = [0] * sum_xp
dp[0] = 1
for i in xp:
    new_dp = [0] * sum_xp
    for j in range(sum_xp - i):
        new_dp[i + j] += dp[j]
    for j in range(sum_xp):
        dp[j] += new_dp[j]

for i in xm:
    new_dp = [0] * sum_xp
    for j in range(i, sum_xp):
        new_dp[j - i] += dp[j]
    for j in range(sum_xp):
        dp[j] += new_dp[j]

print(dp[0] * pow(2, num_zero) - 1)