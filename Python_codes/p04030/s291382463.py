s = list(input())
out = []

for s1 in s:
	if s1 == 'B':
		if out != []:
			out.pop()
	else:
		out.append(s1)
print(''.join(out))