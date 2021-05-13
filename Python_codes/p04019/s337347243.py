x = input()
n = x.count('N')
e = x.count('E')
w = x.count('W')
s = x.count('S')
if ((n and not s) or (not n and s) or (w and not e) or (not w and e)):
	print("No")
else:
	print("Yes")