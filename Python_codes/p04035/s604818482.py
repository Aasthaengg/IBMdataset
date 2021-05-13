n, l = map(int, input().split())
a = list(map(int, input().split()))

if n == 2:
	if a[0] + a[1] < l:
		print("Impossible")
	else:
		print("Possible")
		print(1)

else:
	nagai = 0
	for i in range(n - 1):
		if a[i] + a[i + 1] > nagai:
			nagai = a[i] + a[i + 1]
			nagai_index = i + 1

	if nagai < l:
		print("Impossible")
	else:
		print("Possible")
		for i in range(1, nagai_index):
			print(i)
		for i in range(n - 1, nagai_index, -1):
			print(i)
		print(nagai_index)