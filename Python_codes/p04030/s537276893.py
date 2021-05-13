S = input()
ans = ''
for s in S:
	if s == 'B':
		if len(ans) != 0:
			ans = ans[:-1]
	else:
		ans += s
print(ans)