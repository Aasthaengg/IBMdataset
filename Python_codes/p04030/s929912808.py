s = []
for l in raw_input():
	if l == 'B':
		if s:s.pop()
	else:
		s.append(l)
print ''.join(s)