from collections import Counter
if sum(map(lambda x: x%2, Counter(input()).values())) == 0:
	print('Yes')
else:
  print('No')