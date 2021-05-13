s=input()
if (('W' in s)+('E' in s))%2:
	print('No')
elif (('N' in s)+('S' in s))%2:
	print('No')
else:
	print('Yes')