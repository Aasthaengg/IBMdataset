import collections
s = list(input())
c = collections.Counter(s)
for s1 in c.values():
	if s1 % 2 !=0:
		print('No')
		exit()
print('Yes')