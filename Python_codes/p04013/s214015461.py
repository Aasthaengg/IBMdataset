n, a = map(int, input().split())
nums = list(map(lambda x: int(x) - a, input().split()))

dp = {0 : 1}

for n in nums:
	for k, v in list(dp.items()):
		dp[k+n] =dp.get(k+n, 0) + v
print(dp[0] - 1)
