n, k = map(int, raw_input().split())
l = map(int, raw_input().split())
ind = -1
for i in range(n - 1):
	if l[i] + l[i + 1] >= k:
		ind = i
		break
if ind == -1:
	print "Impossible"
else:
	print "Possible"
	for i in range(1, ind + 1):
		print i 
	for i in range(n - 1, ind, -1):
		print i 