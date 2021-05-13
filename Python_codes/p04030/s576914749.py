s = input()
ans = []
for i in s:
	if i=='B':
		if len(ans)==0:
			continue
		ans.pop()
	else:
		ans.append(i)
new = ''.join(ans)
print(new)